import pandas as pd
import joblib
import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load model and scaler
model = joblib.load(os.path.join(BASE_DIR, "std_performance_model.pkl"))
scaler = joblib.load(os.path.join(BASE_DIR, "scaler.pkl"))

# New data
new_data = {
    "Hours Studied": 8,
    "Previous Scores": 170,
    "Extracurricular Activities Mapped": 1,
    "Sleep Hours": 6,
    "Sample Question Papers Practiced": 15
}

def predict_std_performence(new_data):

    # Convert to DataFrame
    X_new = pd.DataFrame([new_data])

    # --- SCALE first: only numeric columns that were scaled during training ---
    numeric_cols_to_scale = ["Hours Studied", "Previous Scores", "Sleep Hours", "Sample Question Papers Practiced"]
    X_new[numeric_cols_to_scale] = scaler.transform(X_new[numeric_cols_to_scale])

    # --- THEN reorder columns for model ---
    X_new = X_new[model.feature_names_in_]

    # Predict
    prediction = model.predict(X_new)[0]

    return prediction

# print("Predicted Standardized Performance:", end=" ")
# print(predict_std_performence(new_data))
def get_model_performance():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(BASE_DIR, "regression_metrics.json"), "r") as f:
        metrics = json.load(f)   # loads into a Python dict
    return metrics

# Example usage
# print("Model Performance Metrics:")
# print(get_model_performance()['r2_score'])
# print(get_model_performance()['mse'])
# print(get_model_performance()['rmse'])
# print(get_model_performance()['mae'])

# This block will only run when executing this file directly (e.g. python titanic_predict.py)
if __name__ == "__main__":
    # test code (won’t run in Django)
    predict_std_performence(new_data)
    get_model_performance()