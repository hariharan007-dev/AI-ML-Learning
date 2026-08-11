import pandas as pd

df = pd.read_csv(
    "data/SMSSpamCollection",
    sep="\t",
    header=None,
    names=["label", "message"]
)
print("before clean:",df.shape)
#remove duplicate
df = df.drop_duplicates()
#remove null
df = df.dropna()

print("After clean:",df.shape)

print("Label distribution:")
print(df["label"].value_counts())

