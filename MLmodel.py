import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report

# ==============================
# Load Dataset
# ==============================
df = pd.read_csv("C:/Users/K KHYATHIPRIYA/OneDrive/Documents/Desktop/IOMP/02-14-2018.csv")

# Drop non-numeric columns 
if "Timestamp" in df.columns:
    df = df.drop(columns=["Timestamp"])

# Replace infinite values
df.replace([np.inf, -np.inf], np.nan, inplace=True)
df.dropna(inplace=True)

# ==============================
# Feature / Label Separation
# ==============================
X = df.drop("Label", axis=1)
y = df["Label"].apply(lambda x: 0 if x == "Benign" else 1)

# ==============================
# Train-Test Split
# ==============================
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# ==============================
# Scaling
# ==============================
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# ==============================
# Model Training
# ==============================
model = RandomForestClassifier(
    n_estimators=150,
    max_depth=30,
    n_jobs=-1,
    random_state=42
)

model.fit(X_train, y_train)

# ==============================
# Evaluation
# ==============================
y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))

# ==============================
# Save Model & Scaler
# ==============================
joblib.dump(model, "ids_model.pkl")
joblib.dump(scaler, "scaler.pkl")

print("Model and scaler saved successfully.")     