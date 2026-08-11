import pandas as pd

df = pd.read_csv(
    "data/SMSSpamCollection",
    sep="\t",
    header=None,
    names=["label", "message"]
)

print(df.head())
print()
print("Dataset shape:", df.shape)
print("duplicate rows:")
print(df.isnull().sum())
print("Label distribution:")
print(df["label"].value_counts())