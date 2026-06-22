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

- Monitors network traffic in real time
- Detects malicious activity using a trained ML model
- Applies an **Agentic AI decision engine** to autonomously classify threats and suggest responses
- Displays live results on an interactive **Streamlit dashboard**

> Built using the **CICIDS dataset** — a benchmark cybersecurity dataset with real-world attack scenarios.

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
Prediction Output (Benign / Attack)
        ↓
Agentic AI Decision Engine
        ↓
Risk Evaluation → Action Selection
        ↓
Streamlit Dashboard + Alerts
```

---

## 📂 Dataset — CICIDS

The **CICIDS (Canadian Institute for Cybersecurity Intrusion Detection System)** dataset contains labeled network traffic flows representing both normal and attack behaviour.

> ⚠️ **Note:** The dataset is too large to include in this repository. Download it directly from Kaggle:
>
> [![Kaggle]([https://img.shields.io/badge/Download%20Dataset-Kaggle-20BEFF?style=for-the-badge&logo=kaggle&logoColor=white)](https://www.kaggle.com/datasets/cicdataset/cicids2017](https://www.kaggle.com/datasets/ericanacletoribeiro/cicids2017-cleaned-and-preprocessed/data))
>
> After downloading, place the CSV files in the project root directory before running.

| Class | Description |
|---|---|
| Benign | Normal network traffic |
| FTP Brute Force | Unauthorized FTP login attempts |
| SSH Brute Force | Unauthorized SSH login attempts |

---

## 🔍 Features Used

The model analyzes the following network behaviour features:

- Flow Duration & Packet Length Statistics
- Flow Bytes per Second & Packets per Second
- Inter-arrival Time (IAT)
- Protocol Type
- Connection Flags — SYN, ACK, FIN

---

## 🤖 Agentic AI Decision Engine

The agent acts as an autonomous cybersecurity assistant with the following workflow:

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

---

## 🌐 Streamlit Dashboard

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

### 3. Run the Application
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
├── MLmodel.py                # ML model training
├── backend.py                # Backend processing
├── realtime_detection.py     # Real-time detection logic
├── ids_model.pkl             # Trained ML model
├── scaler.pkl                # Feature scaler
├── attack_logs.csv           # Attack event logs
├── traffic_logs.csv          # Network traffic logs
├── requirements.txt          # Dependencies
└── assets/                   # Screenshots
```

---

## 🚀 Future Enhancements

- [ ] Real-time live network traffic monitoring
- [ ] Integration with firewall automation systems
- [ ] Deep learning-based intrusion detection (LSTM / CNN)
- [ ] Cloud deployment on AWS / Azure
- [ ] Multi-agent cybersecurity architecture
- [ ] Automated IP blocking mechanism

---

## 🧰 Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core language |
| Scikit-learn | ML model (Random Forest) |
| Pandas & NumPy | Data processing |
| Matplotlib | Visualization |
| Streamlit | Interactive dashboard |

---

## 👩‍💻 Author

**Khyathi Priya Kamireddi**
B.Tech — Computer Science Engineering (AI & ML)

[![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)](https://github.com/Khyathi-Priya)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/khyathi-priya-kamireddi-83144a2b8/)

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).
