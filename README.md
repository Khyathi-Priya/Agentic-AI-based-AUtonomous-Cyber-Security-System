<div align="center">

# 🛡️ Agentic AI-Based Autonomous Cybersecurity System

**An intelligent system that monitors network traffic, detects cyber threats, and responds autonomously using Agentic AI principles.**

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)

[![GitHub stars](https://img.shields.io/github/stars/Khyathi-Priya/Agentic-AI-based-AUtonomous-Cyber-Security-System?style=flat&color=6C63FF)](https://github.com/Khyathi-Priya/Agentic-AI-based-AUtonomous-Cyber-Security-System/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/Khyathi-Priya/Agentic-AI-based-AUtonomous-Cyber-Security-System?style=flat&color=6C63FF)](https://github.com/Khyathi-Priya/Agentic-AI-based-AUtonomous-Cyber-Security-System/network)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat)](LICENSE)

</div>

---

## 📌 Overview

Modern cyber attacks are growing in complexity, making rule-based systems ineffective. This project builds an **AI-driven autonomous cybersecurity system** that:

- 🔍 Monitors network traffic in real time
- 🤖 Detects malicious activity using a trained **Random Forest ML model**
- 🧠 Applies an **Agentic AI decision engine** to autonomously classify threats and suggest responses
- 📊 Displays live results on an interactive **Streamlit dashboard**

> Built using the **CICIDS 2017 dataset** — a benchmark cybersecurity dataset with real-world attack scenarios.

---

## 📸 Screenshots

### 🖥️ Dashboard View
![Dashboard](assets/main%20output.png)

### ⚠️ Threat Detection Output
![Threat Detection](assets/threat%20detected.png)

### 🤖 Agent Decision & Alert System
![Agent Decision](assets/detection%20records%20and%20agent%20suggestions.png)

---

## 🧠 System Architecture

```
Network Traffic Data
        ↓
Feature Engineering Layer
        ↓
ML Model — Random Forest Classifier
        ↓
Prediction Output (Benign / Attack Type)
        ↓
Agentic AI Decision Engine
        ↓
Risk Evaluation → Action Selection
        ↓
Streamlit Dashboard + Alerts
```

---

## 📂 Dataset — CICIDS 2017

The **CICIDS (Canadian Institute for Cybersecurity Intrusion Detection System) 2017** dataset contains labeled network traffic flows representing both normal and attack behaviour across multiple attack categories.

> ⚠️ **Note:** The dataset is too large to include in this repository. Download it directly from Kaggle:
>
> [![Kaggle](https://img.shields.io/badge/Download%20Dataset-Kaggle-20BEFF?style=for-the-badge&logo=kaggle&logoColor=white)](https://www.kaggle.com/datasets/ericanacletoribeiro/cicids2017-cleaned-and-preprocessed/data)
>
> After downloading, place the CSV files in the project root directory before running.

| Class | Description |
|---|---|
| Benign | Normal network traffic |
| FTP-BruteForce | Unauthorized FTP login attempts |
| SSH-BruteForce | Unauthorized SSH login attempts |

---

## 🔍 Features Used

The model analyzes the following network behaviour features extracted from traffic flows:

| Feature Category | Features |
|---|---|
| Flow Statistics | Flow Duration, Flow Bytes/s, Flow Packets/s |
| Packet Length | Min, Max, Mean, Std of packet lengths |
| Inter-Arrival Time (IAT) | Mean, Std, Max, Min IAT |
| Protocol & Flags | Protocol Type, SYN, ACK, FIN flag counts |

---

## 🤖 ML Model — Random Forest Classifier

The core detection engine is a **Random Forest Classifier** trained on the CICIDS 2017 dataset.

### Why Random Forest?
- Handles high-dimensional network traffic data effectively
- Robust to noise and outliers in network flows
- Provides feature importance scores for interpretability
- Resistant to overfitting compared to single decision trees

### Training Pipeline (`MLmodel.py`)

```
Raw CSV Data (CICIDS 2017)
        ↓
Data Preprocessing
  → Drop null/infinite values
  → Encode labels (LabelEncoder)
  → Scale features (StandardScaler)
        ↓
Train/Test Split (80/20)
        ↓
Random Forest Training
  → n_estimators: 100 trees
  → criterion: gini impurity
        ↓
Model Serialization
  → ids_model.pkl  (trained classifier)
  → scaler.pkl     (fitted StandardScaler)
```

### Model Artifacts

| File | Description |
|---|---|
| `ids_model.pkl` | Serialized trained Random Forest model |
| `scaler.pkl` | Fitted StandardScaler for consistent feature normalization |

### How Predictions Work

At inference time (`realtime_detection.py`):
1. Raw traffic features are loaded and cleaned
2. `scaler.pkl` normalizes the feature vector
3. `ids_model.pkl` outputs a class label — `Benign` or an attack type
4. The prediction and confidence score are passed to the Agentic AI engine

> 📌 **To retrain the model**, run `MLmodel.py` after placing the CICIDS dataset CSVs in the project root. New `ids_model.pkl` and `scaler.pkl` files will be generated automatically.

---

## 🧠 Agentic AI Decision Engine (`AgenticAI.py`)

The agent acts as an autonomous cybersecurity assistant, wrapping the ML prediction in intelligent decision logic:

```
Observe → Analyze → Decide → Act
```

**Decision Logic:**
```
IF prediction == "Attack":
    IF confidence > threshold:
        → Trigger High Alert
        → Log Security Event
        → Suggest Mitigation (Monitor / Block IP / Raise Alert)
    ELSE:
        → Monitor Closely
ELSE:
    → Mark as Normal Traffic
```

### Agent Response Actions

| Threat Level | Condition | Action |
|---|---|---|
| 🟢 Normal | Benign prediction | Log as normal traffic |
| 🟡 Low | Attack, low confidence | Monitor closely |
| 🔴 High | Attack, high confidence | Trigger alert + suggest mitigation |

---

## 🌐 Streamlit Dashboard (`app.py`)

The interactive dashboard provides:

- ✅ Live prediction display
- ✅ Attack classification results
- ✅ Agent decision & suggested actions
- ✅ Detection records & event logs
- ✅ System status monitoring

---

## ⚙️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/Khyathi-Priya/Agentic-AI-based-AUtonomous-Cyber-Security-System.git
cd Agentic-AI-based-AUtonomous-Cyber-Security-System
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Download the Dataset
Download from [Kaggle](https://www.kaggle.com/datasets/ericanacletoribeiro/cicids2017-cleaned-and-preprocessed/data) and place the CSV files in the project root.

### 4. Train the Model *(skip if using pre-trained `ids_model.pkl`)*
```bash
python MLmodel.py
```

### 5. Run the Application
```bash
streamlit run app.py
```

---

## 📁 Project Structure

```
Agentic-AI-based-AUtonomous-Cyber-Security-System/
│
├── app.py                    # Streamlit dashboard
├── AgenticAI.py              # Agentic AI decision engine
├── MLmodel.py                # ML model training (Random Forest)
├── backend.py                # Backend processing
├── realtime_detection.py     # Real-time detection logic
├── ids_model.pkl             # Trained Random Forest model
├── scaler.pkl                # Fitted feature scaler
├── attack_logs.csv           # Attack event logs
├── traffic_logs.csv          # Network traffic logs
├── requirements.txt          # Python dependencies
└── assets/                   # Screenshots
```

---

## 🧰 Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core language |
| Scikit-learn | ML model (Random Forest Classifier) |
| Pandas & NumPy | Data loading & feature processing |
| Matplotlib | Visualization |
| Streamlit | Interactive real-time dashboard |
| Joblib | Model serialization (`ids_model.pkl`, `scaler.pkl`) |

---

## 🚀 Future Enhancements

- [ ] Add model evaluation metrics (accuracy, precision, recall, F1-score)
- [ ] Real-time live network packet capture (using `scapy` or `pyshark`)
- [ ] Integration with firewall automation (e.g., `iptables`, AWS Security Groups)
- [ ] Deep learning-based intrusion detection (LSTM / CNN)
- [ ] Cloud deployment on AWS / Azure
- [ ] Multi-agent cybersecurity architecture
- [ ] Automated IP blocking mechanism

---

## 👩‍💻 Author

**Khyathi Priya Kamireddi**  
B.Tech — Computer Science Engineering (AI & ML)

[![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)](https://github.com/Khyathi-Priya)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/khyathi-priya-kamireddi-83144a2b8/)

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).
