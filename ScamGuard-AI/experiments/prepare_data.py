import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
df = pd.read_csv(
    "data/SMSSpamCollection",
    sep="\t",
    header=None,
    names=["label", "message"]
)
df = df.drop_duplicates()
df = df.dropna()

le = LabelEncoder()
df["label"] = le.fit_transform(df["label"])

x = df["message"]
y = df["label"]

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42,stratify=y)

print("total message:",len(df))
print("train message:",len(x_train))
print("test message:",len(x_test))
