ScamGuard AI

A machine learning project that detects whether a text message is likely to be a SCAM or SAFE.

This project was built as a learning project to understand how an NLP machine learning model can be trained and connected to a Flask web application.

What I Learned

Through this project, I practiced:

- Python
- Data preprocessing
- Natural Language Processing (NLP)
- TF-IDF
- Machine Learning
- LinearSVC
- Model evaluation
- Decision scores
- Joblib
- Flask
- Connecting a machine learning model to a web application
- Basic threat/risk analysis

How It Works

The basic pipeline is:

User Message
     ↓
Text Preprocessing
     ↓
TF-IDF Vectorization
     ↓
LinearSVC Model
     ↓
Prediction
     ↓
Decision Score
     ↓
Threat Analysis
     ↓
SCAM / SAFE Result

Technologies Used

- Python
- Pandas
- Scikit-learn
- TF-IDF
- LinearSVC
- Joblib
- Flask
- HTML
- CSS
- JavaScript

Project Structure

ScamGuard-AI/
│
├── data/
│   └── Dataset files
│
├── experiments/
│   └── Experimental notebooks/scripts
│
├── model/
│   ├── scam_model.pkl
│   └── tfidf_vector.pkl
│
├── templates/
│   └── index.html
│
├── app.py
├── train_model.py
├── test_model.py
├── threat_analysis.py
├── model_result.txt
└── README.md

Model

The project uses TF-IDF (Term Frequency–Inverse Document Frequency) to convert text messages into numerical features.

A LinearSVC classifier is then used to classify the messages as:

- "SCAM"
- "SAFE"

The model also provides a "decision_function()" score. This score indicates how strongly the classifier leans toward one of the classes.

Example

A scam-like message:

Congratulations! You have won £1000 cash prize.
Call 09061701939 now to claim your reward.

Result:

SCAM
Decision score: 1.47467991

A normal message:

Hey bro, are you coming to college tomorrow?

Result:

SAFE
Decision score: -1.17246146

Threat Analysis

After the ML model makes its prediction, the project performs basic threat analysis to provide additional information such as:

- Risk level
- Indicator
- Decision score

This is a simple rule-based layer built on top of the machine learning prediction.

Flask Web Application

The trained model is connected to a Flask backend.

The application:

1. Receives a message from the web interface.
2. Converts the message using the trained TF-IDF vectorizer.
3. Sends the features to the trained LinearSVC model.
4. Gets the prediction and decision score.
5. Runs the threat analysis.
6. Returns the result to the frontend.

How to Run

1. Clone the repository

git clone <your-repository-url>

2. Open the ScamGuard-AI folder

cd AI-ML-Learning/ScamGuard-AI

3. Create a virtual environment

python -m venv venv

4. Activate the virtual environment

Windows:

venv\Scripts\activate

5. Install the required libraries

pip install pandas scikit-learn flask joblib

6. Run the Flask application

python app.py

Then open the local address shown by Flask in your browser.

Model Testing

The model can also be tested directly from the terminal:

python test_model.py

The test program supports multi-line messages. Enter "END" on a new line to finish the message.

Type:

exit

to stop the program.

Limitations

This project is a learning implementation and should not be treated as a production-grade scam detection system.

Some limitations include:

- The model depends heavily on the training dataset.
- It can incorrectly classify unfamiliar messages.
- Decision scores should not be interpreted as guaranteed probabilities.
- The threat analysis is basic.
- Real-world scam detection would require more diverse and continuously updated data.
- No model can guarantee that a message is completely safe.

Future Improvements

Possible improvements include:

- Improve the training dataset
- Add more types of scam messages
- Compare multiple ML algorithms
- Improve text preprocessing
- Add better evaluation metrics
- Add confusion matrix and classification report
- Improve threat analysis
- Add URL detection
- Add suspicious phone-number detection
- Add explainable predictions
- Deploy the application

Project Purpose

ScamGuard AI is primarily a learning project.

The goal was not to build a perfect scam detection product, but to understand the process of taking a machine learning model from:

Dataset
   ↓
Preprocessing
   ↓
Training
   ↓
Testing
   ↓
Saved Model
   ↓
Flask Integration
   ↓
Web Application

This project is part of my AI/ML learning journey.