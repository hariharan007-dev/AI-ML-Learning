import pandas as pd

data = pd.read_csv('data/games.csv')
print(data.head())

print("\nColumns:")
print(data.columns)

print("\nDataset shape:")
print(data.shape)

print("\nMissing values:")
print(data.isnull().sum())


print(data[data["Title"].str.contains("Sekiro", case=False, na=False)][
    ["Title", "Genres", "Summary"]
])

print(data[data["Title"].str.contains("Spider-Man", case=False, na=False)][
    ["Title", "Genres", "Summary"]
])