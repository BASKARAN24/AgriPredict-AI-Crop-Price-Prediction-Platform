import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle
import os

# 1. SETUP PATHS (Fixes FileNotFoundError)
# This finds the directory where this script is actually located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Assumes 'crop_recommendation.csv' is in the SAME folder as this script
data_path = os.path.join(BASE_DIR, "crop_recommendation.csv")
model_path = os.path.join(BASE_DIR, "recommend_model.pkl")

print(f"Looking for data at: {data_path}")

try:
    # 2. LOAD DATA
    df = pd.read_csv(data_path)
    print("Dataset loaded successfully!")

    # 3. PREPARE DATA
    # Features: N, P, K, temperature, humidity, ph, rainfall
    X = df[['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']]
    y = df['label'] # Target: Crop name

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 4. TRAIN MODEL
    print("Training the Random Forest model (this may take a few seconds)...")
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # 5. EVALUATE
    accuracy = model.score(X_test, y_test)
    print(f"Training Complete! Accuracy: {accuracy * 100:.2f}%")

    # 6. SAVE MODEL
    with open(model_path, "wb") as f:
        pickle.dump(model, f)
    
    print(f"Model saved as: {model_path}")

except FileNotFoundError:
    print("ERROR: 'crop_recommendation.csv' not found.")
    print(f"Please make sure the file is in: {BASE_DIR}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")