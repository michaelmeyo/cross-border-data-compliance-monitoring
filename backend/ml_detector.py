import os
import joblib
import numpy as np

# Get correct model path dynamically
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "models", "bot_model.pkl")

model = joblib.load(MODEL_PATH)

def detect_anomaly(request_count):

    data = np.array([[request_count]])

    prediction = model.predict(data)

    if prediction[0] == -1:
        return True

    return False