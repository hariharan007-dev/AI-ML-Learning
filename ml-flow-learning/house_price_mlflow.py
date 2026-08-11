import pandas as pd
import mlflow
import mlflow.sklearn

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error, r2_score

# ✅ Set these FIRST before any other mlflow calls
mlflow.set_tracking_uri("http://127.0.0.1:5000")
mlflow.set_experiment("House Price Prediction")
print("updated mlflow tracking uri and experiment name")

# Load dataset
df = pd.read_csv("california_housing.csv")

# X and y
X = df.drop(["median_house_value", "ocean_proximity"], axis=1)
y = df["median_house_value"]

# Fill missing values
X = X.fillna(X.mean())

# Parameters
test_size = 0.2
n_estimators=100,
max_depth=10,
random_state=0

# Train test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=test_size, random_state=random_state
)

print("Training data:", X_train.shape)
print("Testing data:", X_test.shape)

# Create model
from sklearn.ensemble import RandomForestRegressor
model = RandomForestRegressor(
    n_estimators=100,
    max_depth=10,
    random_state=0
)
# Start MLflow run
with mlflow.start_run():

    mlflow.log_param("model", "RandomForestRegressor")
    mlflow.log_param("test_size", test_size)
    mlflow.log_param("random_state", random_state)

    model.fit(X_train, y_train)
    print("Model trained")

    predictions = model.predict(X_test)

    mse = mean_squared_error(y_test, predictions)
    r2 = r2_score(y_test, predictions)

    print("MSE:", mse)
    print("R2:", r2)

    mlflow.log_metric("MSE", mse)
    mlflow.log_metric("R2", r2)

    mlflow.sklearn.log_model(
        model,
        name="random_forest_model"
    )
    print("Model logged to MLflow")

    print("\nActual vs Predicted:")
    for i in range(5):
        print(f"Actual: {y_test.iloc[i]}, Predicted: {predictions[i]}")