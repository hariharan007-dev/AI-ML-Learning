import joblib

model = joblib.load("model/scam_model.pkl")
vector = joblib.load("model/tfidf_vector.pkl")

print("ScamAI is imported")
print("Type END on a new line when finished")
print("Type exit to stop\n")

while True:

    print("\nENTER YOUR MESSAGE:")

    lines = []

    while True:
        line = input()

        if line == "END":
            break

        lines.append(line)

    message = "\n".join(lines)

    if message.strip().lower() == "exit":
        break

    message_tfidf = vector.transform([message])

    prediction = model.predict(message_tfidf)[0]
    score =model.decision_function(message_tfidf)

    if prediction == 1:
        print("\nSCAM!")
    else:
        print("\nSAFE")

    print("decision score:",score)