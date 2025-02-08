import os
import pandas as pd
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
import torch.nn.functional as F
from typing import List
import numpy as np

# Tokenizer Class

class IngredientTokenizer:
    def __init__(self, unk_token="<unk>"):
        self.ingredient_to_id = {}
        self.id_to_ingredient = {}
        self.fitted = False
        self.unk_token = unk_token

    def fit(self, ingredient_lists: List[List[str]], main_ingredients: List[str]):
        unique_ingredients = set()
        for ingr_list in ingredient_lists:
            for ingr in ingr_list:
                ingr = ingr.strip().lower()
                unique_ingredients.add(ingr)

        for mi in main_ingredients:
            mi = mi.strip().lower()
            unique_ingredients.add(mi)

        unique_ingredients = sorted(list(unique_ingredients))

        unique_ingredients = [self.unk_token] + unique_ingredients

        self.ingredient_to_id = {ingr: i for i, ingr in enumerate(unique_ingredients)}
        self.id_to_ingredient = {i: ingr for ingr, i in self.ingredient_to_id.items()}
        self.fitted = True

    def transform(self, ingredient_list: List[str]) -> List[int]:
        if not self.fitted:
            raise ValueError("Tokenizer not fitted yet.")
        token_ids = []
        for ing in ingredient_list:
            ing = ing.strip().lower()
            token_ids.append(self.ingredient_to_id.get(ing, self.ingredient_to_id[self.unk_token]))
        return token_ids

    def transform_single(self, ingredient: str) -> int:
        ingredient = ingredient.strip().lower()
        return self.ingredient_to_id.get(ingredient, self.ingredient_to_id[self.unk_token])

    def vocab_size(self):
        return len(self.ingredient_to_id)

# Dataset Class

class CocktailDataset(Dataset):
    def __init__(self, csv_path: str, tokenizer: IngredientTokenizer):
        self.data = pd.read_csv(csv_path)
        self.data['ingredient_list'] = self.data['ingredients'].apply(lambda x: [i.strip() for i in x.split(',')])

        ingredient_lists = self.data['ingredient_list'].tolist()
        main_ingredients = self.data['main_ingredient'].tolist()

        if not tokenizer.fitted:
            tokenizer.fit(ingredient_lists, main_ingredients)

        self.tokenizer = tokenizer

        self.data['ingredient_tokens'] = self.data['ingredient_list'].apply(self.tokenizer.transform)
        self.data['main_token'] = self.data['main_ingredient'].apply(self.tokenizer.transform_single)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        row = self.data.iloc[idx]
        ingredient_tokens = row['ingredient_tokens']
        main_token = row['main_token']
        cocktail_name = row['cocktail_name']

        ingredient_tokens_tensor = torch.tensor(ingredient_tokens, dtype=torch.long)
        main_token_tensor = torch.tensor(main_token, dtype=torch.long)
        return ingredient_tokens_tensor, main_token_tensor, cocktail_name

# Model Class

class CocktailEmbeddingModel(nn.Module):
    def __init__(self, vocab_size: int, embedding_dim: int = 50):
        super(CocktailEmbeddingModel, self).__init__()
        self.ingredient_emb = nn.Embedding(num_embeddings=vocab_size, embedding_dim=embedding_dim)
        self.fc = nn.Linear(embedding_dim, embedding_dim)

    def forward(self, ingredient_tokens, main_token):
        ingr_embs = self.ingredient_emb(ingredient_tokens)  # [N_ingr, embedding_dim]
        ingr_vector = ingr_embs.mean(dim=0)  # average embedding
        main_emb = self.ingredient_emb(main_token)  # [embedding_dim]
        combined = (ingr_vector + main_emb) / 2
        return self.fc(combined)

# Recommender Class

class CocktailRecommender:
    def __init__(self, csv_path: str, embedding_dim: int = 50, batch_size: int = 32, epochs: int = 5):
        self.csv_path = csv_path
        self.embedding_dim = embedding_dim
        self.batch_size = batch_size
        self.epochs = epochs

        self.tokenizer = IngredientTokenizer()
        self.model = None
        self.cocktail_embeddings = {}
        self.all_main_ingredients = []
        self.cocktail_details = {}  # name -> (ingredient_list, main_ingredient)
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    def load_data_and_train_model(self):
        dataset = CocktailDataset(self.csv_path, self.tokenizer)
        dataloader = DataLoader(dataset, batch_size=self.batch_size, shuffle=True, collate_fn=self.collate_fn)

        self.all_main_ingredients = sorted(set(dataset.data['main_ingredient'].str.strip().str.lower()))

        vocab_size = self.tokenizer.vocab_size()
        self.model = CocktailEmbeddingModel(vocab_size, embedding_dim=self.embedding_dim).to(self.device)

        optimizer = optim.Adam(self.model.parameters(), lr=0.001)

        for epoch in range(self.epochs):
            self.model.train()
            total_loss = 0
            for ingr_tokens, main_token, _ in dataloader:
                ingr_tokens = [x.to(self.device) for x in ingr_tokens]
                main_token = main_token.to(self.device)
                optimizer.zero_grad()

                loss_batch = 0
                for i in range(len(ingr_tokens)):
                    out = self.model(ingr_tokens[i], main_token[i])
                    target_emb = self.model.ingredient_emb(ingr_tokens[i]).mean(dim=0)
                    loss = F.mse_loss(out, target_emb)
                    loss.backward()
                    loss_batch += loss.item()
                optimizer.step()
                total_loss += loss_batch

            print(f"Epoch {epoch + 1}/{self.epochs}, Loss: {total_loss:.4f}")

        self.encode_all_cocktails(dataset)

    def encode_all_cocktails(self, dataset):
        self.model.eval()
        with torch.no_grad():
            for i in range(len(dataset)):
                ingr_tokens, main_token, name = dataset[i]
                emb = self.model(ingr_tokens.to(self.device), main_token.to(self.device)).cpu().numpy()
                self.cocktail_embeddings[name] = emb

                row = dataset.data.iloc[i]
                ingredients = row['ingredient_list']
                main_ingredient = row['main_ingredient']
                self.cocktail_details[name] = (ingredients, main_ingredient)

    def query(self, ingredients: List[str], main_ingredient: str):
        ingr_tokens = self.tokenizer.transform(ingredients)
        main_token = self.tokenizer.transform_single(main_ingredient)
        ingr_tokens_t = torch.tensor(ingr_tokens, dtype=torch.long, device=self.device)
        main_token_t = torch.tensor(main_token, dtype=torch.long, device=self.device)

        self.model.eval()
        with torch.no_grad():
            query_emb = self.model(ingr_tokens_t, main_token_t).cpu().numpy()

        results = []
        for name, emb in self.cocktail_embeddings.items():
            sim = self.cosine_similarity(query_emb, emb)
            results.append((name, sim))
        results.sort(key=lambda x: x[1], reverse=True)
        return results[:5]

    @staticmethod
    def cosine_similarity(a, b):
        return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

    @staticmethod
    def collate_fn(batch):
        ingr_tokens_list = [item[0] for item in batch]
        main_tokens = torch.tensor([item[1] for item in batch], dtype=torch.long)
        names = [item[2] for item in batch]
        return ingr_tokens_list, main_tokens, names

if __name__ == "__main__":
    csv_path = r"C:\Users\Warren\Desktop\Python_Nesteruk\hotaling_data_clean.csv"
    recommender = CocktailRecommender(csv_path=csv_path, embedding_dim=50, batch_size=8, epochs=3)
    recommender.load_data_and_train_model()

    user_ingredients = []
    print("Enter ingredients (type 'done' when finished):")
    while True:
        inp = input("> ").strip()
        if inp.lower() == 'done':
            break
        user_ingredients.append(inp)

    print("Available main ingredients from the dataset:")
    for mi in recommender.all_main_ingredients:
        print(mi)
    main_ingr = input("Enter main ingredient (from the list above, if possible): ").strip()

    # Get top 5 recommendations
    top_5 = recommender.query(user_ingredients, main_ingr)
    print("\nTop 5 similar cocktails:")
    for name, score in top_5:
        ingredients, main_ing = recommender.cocktail_details[name]
        print(f"Cocktail: {name}")
        print(f"Similarity: {score:.4f}")
        print(f"Ingredients: {', '.join(ingredients)}")
        print(f"Main Ingredient: {main_ing}")
        print("-" * 40)
