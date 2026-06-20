# 🛡️ Agentic AI-Based Autonomous Cybersecurity System

An AI-powered autonomous cybersecurity system that monitors network traffic, detects malicious activity, and performs intelligent response actions using Machine Learning and Agentic AI principles.

---

## ⭐ Key Highlights

* End-to-end cybersecurity ML pipeline
* Real-world CICIDS dataset integration
* Random Forest-based intrusion detection system
* Agentic AI decision-making layer for autonomous response
* Streamlit-based interactive monitoring dashboard
* Automated threat classification and alert system

---

## 🚨 Problem Statement

Modern cyber attacks are becoming increasingly complex and difficult to detect using traditional rule-based systems. These systems rely heavily on manual monitoring and predefined rules, making them ineffective against evolving attack patterns.

There is a need for an intelligent system that can:

* Automatically monitor network traffic
* Detect malicious activity in real time
* Reduce human intervention
* Provide fast and intelligent response actions

---

## 💡 Proposed Solution

This project implements an AI-driven cybersecurity system that:

* Collects and analyzes network traffic data
* Uses a Machine Learning model to detect anomalies
* Classifies traffic into benign or attack categories
* Uses an Agentic AI layer to make autonomous decisions
* Displays results in a real-time Streamlit dashboard

---

## 🧠 System Architecture

```text
Network Traffic Data
        ↓
Feature Engineering Layer
        ↓
Machine Learning Model (Random Forest)
        ↓
Prediction Output
        ↓
Agentic AI Decision Engine
        ↓
Risk Evaluation + Action Selection
        ↓
Streamlit Dashboard + Alerts
```

---

## 📂 Dataset

### CICIDS Dataset

A widely used cybersecurity dataset containing real-world network traffic and attack scenarios.

### Target Classes

| Class           | Description                     |
| --------------- | ------------------------------- |
| Benign          | Normal network traffic          |
| FTP Brute Force | Unauthorized FTP login attempts |
| SSH Brute Force | Unauthorized SSH login attempts |

---

## 🔍 Feature Engineering

The model analyzes multiple network behavior features:

* Flow Duration
* Packet Length Statistics
* Flow Bytes per Second
* Flow Packets per Second
* Inter-arrival Time
* Protocol Type
* Connection Flags (SYN, ACK, FIN)

These features help distinguish normal behavior from attack patterns.

---

## 🧠 Machine Learning Model

### Random Forest Classifier

The system uses a Random Forest model for classification.

### Why Random Forest?

* High accuracy on structured data
* Reduces overfitting
* Handles noisy data effectively
* Works well for intrusion detection tasks

---

## 🤖 Agentic AI Decision Engine

The Agent acts as an autonomous cybersecurity assistant.

### Responsibilities:

* Receives model predictions
* Triggers alerts for suspicious activity
* Logs security events in the dashboard
* Suggests mitigation actions (e.g., monitor traffic, block IP, raise alert)

### Agent Workflow:

```text
Observe → Analyze → Decide → Act
```

---

## 🤖 Agent Decision Logic

IF prediction == "Attack":
    IF confidence > threshold:
        → Trigger High Alert
        → Log Event
        → Suggest Mitigation Action
    ELSE:
        → Monitor Closely

ELSE:
    → Mark as Normal Traffic

    
## 🔐 Threat Detection Process

### Step 1: Data Input

Network traffic data is collected from dataset.

### Step 2: Feature Processing

Relevant network features are extracted.

### Step 3: Model Prediction

Random Forest model classifies traffic.

### Step 4: Agent Decision

Agent evaluates prediction and decides action.

### Step 5: Response

System generates alerts and updates dashboard.

---

## 🌐 User Interface

Built using Streamlit for real-time monitoring.

### Features:

* Live prediction display
* Attack classification results
* System status monitoring
* Visual feedback dashboard

---

## 📸 Screenshots

### 🖥️ 1. Dashboard View

<p align="center">
  <img src="assets/main output.png" width="750"/>
</p>

---

### ⚠️ 2. Threat Detection Output

<p align="center">
  <img src="assets/threat detected.png" width="750"/>
</p>

---

### 🤖 3. Agent Decision / Alert System

<p align="center">
  <img src="assets/detection records and agent suggestions.png" width="750"/>
</p>

## 🌍 Impact

This system demonstrates how artificial intelligence can enhance cybersecurity by reducing manual monitoring, improving detection speed, and enabling autonomous threat response.

---

## 🚀 Future Enhancements

* Real-time network traffic monitoring
* Integration with firewall automation systems
* Deep learning-based intrusion detection models
* Cloud deployment (AWS / Azure)
* Multi-agent cybersecurity systems
* Real-time IP blocking mechanisms

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/Khyathi-Priya/Agentic-AI-based-AUtonomous-Cyber-Security-System.git
```

### Navigate to Project

```bash
cd Agentic-AI-based-AUtonomous-Cyber-Security-System
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run app.py
```

---

## 🧰 Tech Stack

* Python
* Scikit-learn
* Pandas
* NumPy
* Matplotlib
* Streamlit

---

## 📊 Attack Categories

* **Benign:** Normal traffic
* **FTP Brute Force:** FTP login attack attempts
* **SSH Brute Force:** SSH login attack attempts

---

## 👨‍💻 Author

**Khyathi Priya Kamireddi**
B.Tech – Computer Science Engineering (AI & ML)

🔗 GitHub: https://github.com/Khyathi-Priya
🔗 LinkedIn: https://www.linkedin.com/in/khyathi-priya-kamireddi-83144a2b8/

---

## 📜 License

This project is for educational and learning purposes.
