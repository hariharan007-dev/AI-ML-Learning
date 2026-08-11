# 🚀 MLOps House Price Prediction with MLflow

An **MLOps project using MLflow** to track, evaluate, and manage machine learning experiments for a house price prediction system.

## 📌 Project Overview

The main focus of this project is **MLOps and experiment tracking using MLflow**.

A house price prediction model is used as the machine learning use case. MLflow is integrated into the workflow to track experiments, parameters, evaluation metrics, and trained models.

Instead of manually comparing different machine learning experiments, MLflow provides a centralized way to record and compare each run.

```text
                    MLOps Workflow

Dataset
   ↓
Data Preprocessing
   ↓
Train/Test Split
   ↓
Train ML Model
   ↓
       MLflow
   ├── Track Parameters
   ├── Track Metrics
   ├── Track Models
   └── Compare Experiments
   ↓
Best Model
Best Model
🎯 Main Objective

The objective is to demonstrate how MLflow can be used in an MLOps workflow to manage machine learning experiments.

The project demonstrates:

Experiment tracking
Parameter logging
Metric logging
Model logging
Model comparison
Reproducible experiments
🔬 Why MLflow?

When multiple machine learning models are trained with different parameters, it can become difficult to remember which model performed best.

MLflow solves this by recording information about every experiment.

For example:

Run 1
Model: Linear Regression
MAE: ...
R²: ...

Run 2
Model: Random Forest
n_estimators: 100
MAE: ...
R²: ...

Run 3
Model: Random Forest
n_estimators: 200
MAE: ...
R²: ...

These experiments can then be compared through the MLflow UI.

🧠 Machine Learning Use Case

The ML problem used in this project is House Price Prediction.

The model predicts median_house_value using housing and geographical features.

Input Features
longitude
latitude
housing_median_age
total_rooms
total_bedrooms
population
households
median_income
Target
median_house_value
🤖 Machine Learning Model

The initial model is:

Linear Regression

The dataset is divided into:

80% training data
20% testing data

Missing numerical values are handled using the mean of the corresponding column.

📊 Model Evaluation

The model is evaluated using:

MAE — Mean Absolute Error

Measures the average difference between actual and predicted house prices.

R² Score

Measures how well the model explains the variation in the target values.

These metrics are logged into MLflow so that different experiments can be compared.

🛠️ Technologies Used
Python
Pandas
Scikit-learn
MLflow
📂 Project Structure
ML-MLOps/
│
├── california_housing.csv
├── house_price.py
├── README.md
└── mlruns/
🚀 How to Run
1. Install dependencies
pip install pandas scikit-learn mlflow
2. Run the machine learning program
python house_price.py
3. Start the MLflow UI
mlflow ui

Open the MLflow interface in your browser.

📈 MLflow Experiment Tracking

The MLflow dashboard can be used to view:

Experiment runs
Model parameters
MAE
R² score
Saved models
Different model versions

This allows the best experiment to be identified based on its evaluation metrics.

🔮 Future Improvements
Add Random Forest Regression
Add Gradient Boosting Regression
Compare multiple models using MLflow
Perform hyperparameter tuning
Register the best model
Model versioning
Deploy the model using Flask
Create a prediction API
Add model monitoring
Automate the ML pipeline
🎓 Key Concepts Demonstrated
MLOps
Experiment tracking
Model tracking
Model comparison
Reproducibility
Model management
Machine Learning
Regression
Data preprocessing
Missing-value handling
Train/test splitting
Linear Regression
Model evaluation
💡 Project Highlights

The key feature of this project is the integration of MLflow into the machine learning lifecycle.

Rather than building only a house price prediction model, this project demonstrates how machine learning experiments can be tracked, compared, and managed using an MLOps approach.