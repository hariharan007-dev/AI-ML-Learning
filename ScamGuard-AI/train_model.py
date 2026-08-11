import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score,classification_report
#read data
df = pd.read_csv(
    "data/SMSSpamCollection",
    sep="\t",
    header=None,
    names=["label", "message"]
)
#clean data
df = df.drop_duplicates()
df = df.dropna()
#0 or 1 the classification of data
le = LabelEncoder()
df["label"] = le.fit_transform(df["label"])
#seperate data
x = df["message"]
y = df["label"]
#split data
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42,stratify=y)
#convertin text to vector
vector = TfidfVectorizer()
x_train_tfidf = vector.fit_transform(x_train)
x_test_tfidf = vector.transform(x_test)
#model
model = LinearSVC()
model.fit(x_train_tfidf,y_train)
#prediction
y_pred = model.predict(x_test_tfidf)
#accuracy
accuracy = accuracy_score(y_test,y_pred)
print("accuracy:",accuracy)

print("classification report")
print(classification_report(y_test,y_pred))

import joblib
joblib.dump(model,"model/scam_model.pkl")
joblib.dump(vector,"model/tfidf_vector.pkl")
