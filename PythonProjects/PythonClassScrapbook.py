import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

file_path = "C:\\Users\\Warren\\Desktop\\hotaling_cocktails - Cocktails.csv"
df = pd.read_csv(file_path)

#Functions and functions and functions
def data_types():
    print(df.dtypes)

def null_check():
    print("\nMissing values per column:")
    print(df.isnull().sum())

def duplicate_boolean_check(df, column_name):
    duplicates_in_column = df[column_name].duplicated().any()
    print(f"Duplicates in the {column_name} column: ", duplicates_in_column)

def duplicate_identify(df, column_name):
    duplicate_entries = df[df[column_name].duplicated(keep=False)]
    print(f"Duplicate entries in the {column_name}: \n", duplicate_entries)

def remove_duplicate_rows_by_column(df, column_name):
    result = df.drop_duplicates(subset=[column_name])
    return result

def total_duplicate_check ():
    result = df.duplicated().any()
    print(f"Any duplicate data in the set? {result}")

def column_length_check(df, column_name):
    result = df[column_name].count()
    print(f"The length of column {column_name} is {result}")

def reset_dataframe_index(df):
    return df.reset_index(drop=True)

def dataframe_to_numpy_array(df):
    return df.to_numpy()

#A big old mess of data cleaning

data_types()
null_check()
duplicate_boolean_check(df,'Cocktail Name' )
duplicate_boolean_check(df,'Ingredients')
duplicate_identify(df, 'Cocktail Name')
duplicate_identify(df, 'Ingredients')
df = remove_duplicate_rows_by_column(df, 'Cocktail Name')
df = remove_duplicate_rows_by_column(df, 'Ingredients')
df = df[['Cocktail Name','Ingredients']]
null_check()
total_duplicate_check()
column_length_check(df, 'Cocktail Name')
column_length_check(df, 'Ingredients')
df = reset_dataframe_index(df)
print(df)
df = dataframe_to_numpy_array(df)
print(df)

#Extracting the numpy ingredients list and counting the top 10 ingredients.
#I need to do something here so .5 oz of lemon juice vs .75 oz of lemon juice etc. is just lemon juice.

ingredients_list = df[:,1]
all_ingredients = []
for ingredients in ingredients_list:
    all_ingredients.extend([ingredient.strip() for ingredient in ingredients.split(',')])
ingredient_counts = Counter(all_ingredients)
top_ingredients = ingredient_counts.most_common(10)
ingredient_names, counts = zip(*top_ingredients)

#Plotting the top 10 ingredients in a bar chart

plt.figure(figsize=(10, 6))
plt.bar(ingredient_names, counts)
plt.title("Top 10 Most Common Cocktail Ingredients")
plt.xlabel("Ingredients")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()