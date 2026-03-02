import numpy as np
from sklearn.ensemble import IsolationForest
import joblib
import os

# Generate simulated normal traffic
normal_traffic = np.random.normal(loc=5, scale=1, size=(200, 1))

# Train Isolation Forest
model = IsolationForest(contamination=0.1, random_state=42)
model.fit(normal_traffic)

# Save model safely
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "bot_model.pkl")

joblib.dump(model, MODEL_PATH)

print("Model trained and saved successfully.")