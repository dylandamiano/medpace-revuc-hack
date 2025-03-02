# import my pickle objects from ./exports/

import pickle
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestRegressor, BaggingClassifier, AdaBoostClassifier
import joblib

import assistant_backend.openai_assistant as assistant


# Load the trained models
best_bagging: BaggingClassifier = joblib.load("../exports/grid_search_bagging.pkl")
best_boosting: AdaBoostClassifier = joblib.load("../exports/grid_search_boosting.pkl")

PCA_T = joblib.load("../exports/data_transformed.pkl")
NORMALIZED_T = joblib.load("../exports/normalized_data.pkl")
STANDARDIZED_T = joblib.load("../exports/standardized_data.pkl")

# Load test from ./predictions/test_data.csv
test_data = pd.read_csv("../predictions/test_data.csv")

# Predict function (using the following as input: age, wc, sod, bp)

def calculate_gfr(age, sc):
    # Example GFR calculation formula (modify as needed)
    return 186 * (sc ** -1.154) * (age ** -0.203) * 1.212  # Example using MDRD equation for African American males

def predict(age: int, wc: int, sod: int, bp: int, sc: int, bgr: int, pot: int) -> str:
    # Create a DataFrame with the input data
    # Sample data
    data = pd.DataFrame({
        "age": [age],
        "wc": [wc],
        "sod": [sod],
        "bp": [bp],
    })

    # Define your GFR calculation function


    # Apply the GFR calculation to each row
    data['gfr'] = data.apply(lambda row: calculate_gfr(row['age'], sc), axis=1)
    data[['sc', 'bgr', 'pot']] = [sc, bgr, pot] 

    print(data, steps := assistant.retrieve_suggestions(data, age, wc, sod, bp, data['gfr'], sc, bgr, pot))


    # Predict using the trained models
    bagging_prediction = best_bagging.predict(data)
    boosting_prediction = best_boosting.predict(data)

    # Return the predictions
    return f"CKD Stage Bagging prediction: Stage {bagging_prediction[0]}, CKD Stage Boosting prediction: Stage {boosting_prediction[0]}, \n\n Suggested steps: \n {steps}"