import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re


class CocktailDataProcessor:
    def __init__(self, file_path):
        # load the dataset
        self.df = pd.read_csv(file_path, encoding='latin1')
        self.df.name = "hotaling_cocktails - Cocktails - Parsed Ingredients.csv"
        self.original_columns = self.df.columns.tolist()

    def initial_exploration(self):
        # display basic information about the dataset
        print(f"{self.df.name} contains {self.df.shape[0]} rows and {self.df.shape[1]} columns.\n")
        print("First 5 rows of the dataset:")
        print(self.df.head(), "\n")
        print("Basic information about the dataset:")
        self.df.info()
        print("\nSummary Statistics:")
        print(self.df.describe(include='all'))

    def analyze_missing_values(self):
        # calculate the percentage of missing values in each column
        missing_values = self.df.isnull().sum()
        missing_percentage = (missing_values / self.df.shape[0]) * 100
        missing_df = pd.DataFrame({
            'Missing Values': missing_values,
            'Percentage (%)': missing_percentage
        })
        print("\nMissing Values in Each Column:")
        print(missing_df.sort_values(by='Percentage (%)', ascending=False))

    def data_type_conversion(self):
        # convert 'IngredientCount' to int
        self.df['IngredientCount'] = self.df['IngredientCount'].fillna(0).astype(int)
        print("\nData Types of Each Column:")
        print(self.df.dtypes)

    def unique_values_analysis(self):
        # unique values in 'MainAlcohol'
        print("\nUnique values in 'MainAlcohol':")
        print(self.df['MainAlcohol'].unique())
        print(f"\nNumber of unique 'MainAlcohol' values: {self.df['MainAlcohol'].nunique()}")
        # <-- number of unique ingredients
        print(f"\nNumber of unique 'Ingredient' values: {self.df['Ingredient'].nunique()}")
        # Top 20 most frequent ingredients
        print("\nTop 20 most frequent ingredients:")
        print(self.df['Ingredient'].value_counts().head(20))

    def check_duplicates(self):
        # check for duplicate rows
        duplicates = self.df.duplicated()
        num_duplicates = duplicates.sum()
        print(f"\nNumber of duplicate rows: {num_duplicates}")
        if num_duplicates > 0:
            print("\nDuplicate Rows:")
            print(self.df[duplicates])

    def visualize_ingredient_count(self):
        # plot the distribution of 'IngredientCount'
        plt.figure(figsize=(10, 6))
        sns.histplot(self.df['IngredientCount'], bins=30, kde=True)
        plt.title('Distribution of Ingredient Count')
        plt.xlabel('Number of Ingredients')
        plt.ylabel('Frequency')
        plt.show()

    def handle_missing_values(self):
        # handle missing values
        # drop non-essential columns with high missingness
        columns_to_drop = ['Notes', 'Bar/Company', 'Location', 'State', 'Latitude', 'Longitude']
        self.df.drop(columns=columns_to_drop, inplace=True)
        # drop rows with missing 'IsMainAlcohol'
        self.df.dropna(subset=['IsMainAlcohol'], inplace=True)
        # fill missing 'IngredientCount' with 0 and convert to integer
        self.df['IngredientCount'] = self.df['IngredientCount'].fillna(0).astype(int)
        print("\nColumns after dropping non-essential ones:")
        print(self.df.columns)

    def standardize_units(self):
        # function to standardize units in 'Ingredients'
        def standardize_units_in_ingredient(ingredient):
            # convert to lowercase
            ingredient = ingredient.lower()
            # replace variations of 'ounce' with 'oz'
            ingredient = re.sub(r'\bounce(s)?\b', 'oz', ingredient)
            # replace variations of 'milliliter' with 'ml'
            ingredient = re.sub(r'\bmilliliter(s)?\b', 'ml', ingredient)
            # replace variations of 'centiliter' with 'cl'
            ingredient = re.sub(r'\bcentiliter(s)?\b', 'cl', ingredient)
            # replace 'parts' with 'oz'
            ingredient = re.sub(r'\bpart(s)?\b', 'oz', ingredient)
            # standardize 'tablespoon' and 'teaspoon'
            ingredient = re.sub(r'\btablespoon(s)?\b', 'tbsp', ingredient)
            ingredient = re.sub(r'\bteaspoon(s)?\b', 'tsp', ingredient)
            # standardize 'dash' and 'dashes'
            ingredient = re.sub(r'\bdash(es)?\b', 'dash', ingredient)
            # remove extra whitespace
            ingredient = ingredient.strip()
            return ingredient

        # apply the function
        self.df['Ingredients'] = self.df['Ingredients'].apply(standardize_units_in_ingredient)
        print("\nStandardized 'Ingredients':")
        print(self.df['Ingredients'].head(10))

    def normalize_ingredient_names(self):
        # mapping of ingredient variations to standardized names
        ingredient_mapping = {
            'fresh lemon juice': 'lemon juice',
            'juice of a lemon': 'lemon juice',
            'lemon juice freshly squeezed': 'lemon juice',
            'fresh lime juice': 'lime juice',
            'juice of a lime': 'lime juice',
            'lime juice freshly squeezed': 'lime juice',
        }

        def normalize_ingredient(ingredient):
            # replace variants with standardized names
            for variant, standard in ingredient_mapping.items():
                ingredient = ingredient.replace(variant, standard)
            return ingredient

        # remove common descriptors
        def remove_descriptors(ingredient):
            # remove common descriptors
            descriptors = ['fresh', 'organic', 'squeezed', 'chilled', 'fine', 'premium']
            for descriptor in descriptors:
                ingredient = ingredient.replace(descriptor, '')
            # remove extra whitespace
            ingredient = ' '.join(ingredient.split())
            return ingredient

        # apply the functions
        self.df['Ingredients'] = self.df['Ingredients'].apply(normalize_ingredient)
        self.df['Ingredients'] = self.df['Ingredients'].apply(remove_descriptors)
        print("\nNormalized 'Ingredients':")
        print(self.df['Ingredients'].head(10))

    def save_cleaned_data(self, output_file):
        # save the cleaned DataFrame to a CSV file
        self.df.to_csv(output_file, index=False)
        print(f"\nCleaned data saved to {output_file}")

    @staticmethod
    def parse_ingredient(ingredient_str):
        # regex pattern to extract quantity, unit, and ingredient name
        pattern = r'(?:(\d*\.?\d+)\s*(oz|ml|cl|tbsp|tsp|dash|drop|pinch)?\s*)?(.*)'
        match = re.match(pattern, ingredient_str)
        if match:
            quantity = float(match.group(1)) if match.group(1) else None
            unit = match.group(2) if match.group(2) else ''
            name = match.group(3).strip()
            return pd.Series({'Quantity': quantity, 'Unit': unit, 'Ingredient_Name': name})
        else:
            # if no match, return null values
            return pd.Series({'Quantity': None, 'Unit': None, 'Ingredient_Name': ingredient_str})

    def parse_ingredients(self):
        # apply the parse_ingredient function
        parsed_ingredients = self.df['Ingredients'].apply(self.parse_ingredient)
        # join the parsed columns to the DataFrame
        self.df = pd.concat([self.df, parsed_ingredients], axis=1)
        print("\nParsed Ingredients:")
        print(self.df[['Ingredients', 'Quantity', 'Unit', 'Ingredient_Name']].head(10))

    @staticmethod
    def convert_to_oz(row):
        # convert all ingredient quantities to oz, the King of volumetric fluid measurements
        quantity = row['Quantity']
        unit = row['Unit']
        if pd.isnull(quantity) or unit == '':
            return quantity  # return as is- given no quantity or unit
        else:
            unit = unit.lower()
            conversion_factors = {
                'ml': 0.033814,
                'cl': 0.33814,
                'tbsp': 0.5,
                'tsp': 0.166667,
                'dash': 0.03125,
                'drop': 0.002083,
                'pinch': 0.00520833,
                'oz': 1,
            }
            if unit in conversion_factors:
                return quantity * conversion_factors[unit]
            else:
                return quantity  # if unit not recognized, return quantity as is

    def convert_units_to_oz(self):
        # apply the conversion function
        self.df['Quantity_oz'] = self.df.apply(self.convert_to_oz, axis=1)
        # round the quantities for readability
        self.df['Quantity_oz'] = self.df['Quantity_oz'].round(2)
        print("\nIngredients with Quantities in oz:")
        print(self.df[['Ingredient_Name', 'Quantity_oz']].head(10))

    def visualize_ingredient_quantities(self):
        # plot the distribution of ingredient quantities in ounces
        plt.figure(figsize=(10, 6))
        sns.histplot(self.df['Quantity_oz'].dropna(), bins=30, kde=True)
        plt.title('Distribution of Ingredient Quantities (oz)')
        plt.xlabel('Quantity (oz)')
        plt.ylabel('Frequency')
        plt.show()

        # box plot to identify outliers
        plt.figure(figsize=(10, 6))
        sns.boxplot(x=self.df['Quantity_oz'].dropna())
        plt.title('Box Plot of Ingredient Quantities (oz)')
        plt.xlabel('Quantity (oz)')
        plt.show()

    def visualize_common_ingredients(self, top_n=20):
        # calculate the frequency of each ingredient
        ingredient_counts = self.df['Ingredient_Name'].value_counts().head(top_n)
        # plot the top N ingredients
        plt.figure(figsize=(12, 6))
        sns.barplot(x=ingredient_counts.values, y=ingredient_counts.index)
        plt.title(f'Top {top_n} Most Common Ingredients')
        plt.xlabel('Frequency')
        plt.ylabel('Ingredient')
        plt.show()

    def explore_relationships(self):
        # relationship between Ingredient Count and Main Alcohol
        plt.figure(figsize=(12, 6))
        sns.boxplot(x='MainAlcohol', y='IngredientCount', data=self.df)
        plt.title('Ingredient Count by Main Alcohol Type')
        plt.xlabel('Main Alcohol')
        plt.ylabel('Ingredient Count')
        plt.xticks(rotation=45)
        plt.show()

    def perform_statistical_analysis(self):
        # calculate correlation matrix
        numeric_cols = self.df.select_dtypes(include=['float64', 'int64'])
        corr_matrix = numeric_cols.corr()
        print("\nCorrelation Matrix:")
        print(corr_matrix)

        # visualize correlation matrix
        plt.figure(figsize=(8, 6))
        sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
        plt.title('Correlation Matrix Heatmap')
        plt.show()


if __name__ == "__main__":
    processor = CocktailDataProcessor('hotaling_cocktails.csv')
    processor.initial_exploration()
    processor.analyze_missing_values()
    processor.data_type_conversion()
    processor.unique_values_analysis()
    processor.check_duplicates()
    processor.visualize_ingredient_count()
    processor.handle_missing_values()

    # run all these when viewing visualizations, will be better when i convert to ipynb
    processor.standardize_units()
    processor.normalize_ingredient_names()
    processor.parse_ingredients()
    processor.convert_units_to_oz()

    processor.visualize_ingredient_quantities()

    # string joining cutting off edge of graph? take a peek at this for me
    processor.visualize_common_ingredients()

    processor.explore_relationships()
    processor.perform_statistical_analysis()
    processor.save_cleaned_data('hotaling_cocktails_cleaned.csv')