import pandas as pd
import numpy as np
import joblib
import random
from datetime import datetime

# ==============================
# Load model & scaler
# ==============================
model = joblib.load("ids_model.pkl")
scaler = joblib.load("scaler.pkl")

# ==============================
# Load dataset
# ==============================
df = pd.read_csv("02-14-2018.csv")

if "Timestamp" in df.columns:
    df = df.drop(columns=["Timestamp"])

df.replace([np.inf, -np.inf], np.nan, inplace=True)
df.dropna(inplace=True)

X = df.drop("Label", axis=1)
y = df["Label"]

# ==============================
# Detection Function
# ==============================
def detect_network_flow():
    i = random.randint(0, len(X) - 1)

    flow_id = datetime.now().strftime("%H%M%S%f")

    sample = X.iloc[i].values.reshape(1, -1)
    sample_scaled = scaler.transform(sample)

    prediction_val = model.predict(sample_scaled)[0]

    if prediction_val == 0:
        prediction = "Normal"
        attack_name = "None"
        attack_type = "Benign"
    else:
        prediction = "Attack"
        attack_name = str(y.iloc[i])
        attack_type = "Malicious"

    # Top 3 features influencing (scaled magnitude)
    top_indices = np.argsort(np.abs(sample_scaled[0]))[-3:]
    top_features = [X.columns[idx] for idx in top_indices]

    return flow_id, prediction, attack_type, attack_name, top_features