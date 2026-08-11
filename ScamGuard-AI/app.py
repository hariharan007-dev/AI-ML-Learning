from flask import Flask,request,jsonify,render_template
import joblib
from threat_analysis import analyze_threat

app = Flask(__name__)

#load AI model
model = joblib.load("model/scam_model.pkl")
vector = joblib.load("model/tfidf_vector.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods = ["POST"])
def predict():
    data = request.get_json()
    message = data["message"]
    #message to vector
    message_tfidf = vector.transform([message])
    #prediction
    prediction = model.predict(message_tfidf)[0]
    #get score 
    score = model.decision_function(message_tfidf)[0]
    #indicator
    indicator = analyze_threat(message)

    if prediction == 1:
        result = "SCAM"
        if score >= 1:
          risk = "HIGH"
        else:
          risk = "MEDIUM"
    else:
        result = "SAFE"
        if score<=-1:
          risk = "LOW"
        else:
          risk = "MEDIUM"
    return jsonify({
        "prediction":result,
        "risk":risk,
        "decision_score":score,
        "indicator":indicator
    })
if __name__ == "__main__":
    app.run(debug=True)
   