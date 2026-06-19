# 🛡️ AI-Based Autonomous Cybersecurity Threat Detection System

## 📌 Overview

Cyber attacks are becoming increasingly sophisticated, making traditional rule-based security systems less effective in detecting modern threats. This project presents an AI-powered autonomous cybersecurity system that monitors network traffic, detects malicious activities, and performs intelligent response actions.

The system uses a Machine Learning model trained on network traffic data from the CICIDS dataset to classify traffic as:

- Benign (Normal Traffic)
- FTP Brute Force Attack
- SSH Brute Force Attack

An intelligent agent analyzes the model's predictions and initiates appropriate security actions such as threat alerts and attack mitigation recommendations.

---

## 🎯 Problem Statement

With the rapid growth of internet-connected systems, cyber attacks such as brute force attacks have become increasingly common. Traditional security systems often rely on predefined rules and manual monitoring, making them less effective against evolving threats.

Organizations and individuals require an intelligent system capable of:

- Monitoring network traffic automatically
- Detecting malicious activities in real time
- Reducing human intervention
- Providing faster threat response

---

## 💡 Proposed Solution

This project implements an AI-based cybersecurity monitoring system that:

1. Analyzes network traffic features
2. Detects malicious behavior using Machine Learning
3. Classifies traffic into attack categories
4. Uses an intelligent agent to perform automated response actions
5. Displays results through a Streamlit-based dashboard

The system acts as a smart cybersecurity assistant capable of identifying suspicious patterns and assisting in threat mitigation.

---

## 🏗️ System Architecture

```text
Network Traffic
       │
       ▼
Feature Extraction
       │
       ▼
Random Forest Model
       │
       ▼
Threat Classification
(Benign / FTP Brute Force / SSH Brute Force)
       │
       ▼
Agentic AI Decision Layer
       │
       ▼
Threat Response & Alert
       │
       ▼
Streamlit Dashboard
```

---

## 📂 Dataset

### CICIDS Dataset

This project uses a subset of the CICIDS (Canadian Institute for Cybersecurity Intrusion Detection System) dataset, a widely used cybersecurity dataset containing real-world network traffic and attack scenarios.

### Target Classes

| Class | Description |
|---------|------------|
| Benign | Normal network traffic |
| FTP Brute Force | Password guessing attacks targeting FTP services |
| SSH Brute Force | Password guessing attacks targeting SSH services |

### Why This Dataset?

- Realistic network traffic data
- Well-labeled attack categories
- Widely used in cybersecurity research
- Suitable for intrusion detection systems

---

## 📊 Important Features Used

The model analyzes various network traffic characteristics, including:

### Flow Features
- Flow Duration
- Total Forward Packets
- Total Backward Packets

### Packet Features
- Packet Length Maximum
- Packet Length Minimum
- Packet Length Mean
- Average Packet Size

### Traffic Features
- Flow Bytes per Second
- Flow Packets per Second

### Time-Based Features
- Inter Arrival Time
- Active Time
- Idle Time

### Protocol Features
- Destination Port
- Protocol Type

### Connection Flags
- SYN Flag Count
- ACK Flag Count
- FIN Flag Count

These features help identify behavioral differences between normal traffic and cyber attacks.

---

## 🧠 Machine Learning Model

### Random Forest Classifier

The project uses the Random Forest algorithm for threat classification.

### Why Random Forest?

- High accuracy
- Handles large datasets efficiently
- Reduces overfitting
- Robust against noisy data
- Excellent performance for classification tasks
- Combines multiple decision trees for better predictions

### Working Principle

Random Forest creates multiple decision trees and combines their predictions through majority voting.

Example:

- Tree 1 → FTP Brute Force
- Tree 2 → FTP Brute Force
- Tree 3 → Benign

Final Prediction:

FTP Brute Force

---

## 🤖 Agentic AI Component

This project incorporates Agentic AI concepts.

### What is an Agent?

An agent is an intelligent entity that:

- Observes its environment
- Makes decisions
- Takes actions

### Role of Agentic AI

The agent:

1. Monitors model predictions
2. Identifies potential threats
3. Generates alerts
4. Suggests mitigation actions
5. Assists in autonomous decision-making

### Agent Workflow

```text
Observe → Analyze → Decide → Act
```

### Benefits

- Reduced human intervention
- Faster threat response
- Intelligent monitoring
- Autonomous security assistance

---

## 🔍 Threat Detection Process

### Step 1: Data Collection

Network traffic data is collected from the dataset.

### Step 2: Feature Extraction

Important network characteristics are extracted.

### Step 3: Model Prediction

The Random Forest model analyzes traffic patterns.

### Step 4: Classification

Traffic is classified into:

- Benign
- FTP Brute Force
- SSH Brute Force

### Step 5: Agent Response

The intelligent agent:

- Generates alerts
- Flags suspicious activities
- Suggests security actions

---

## 🌐 User Interface

The application is built using Streamlit.

### Why Streamlit?

- Fast development
- Easy Python integration
- Minimal code requirement
- Excellent support for Machine Learning applications
- Interactive dashboards

### Dashboard Features

- Threat detection results
- Prediction visualization
- Attack classification display
- System monitoring interface

---

## 🚀 Installation

### Clone Repository

```bash
git clone https://github.com/Khyathi-Priya/Agentic-AI-based-AUtonomous-Cyber-Security-System.git
```

### Navigate to Project Directory

```bash
cd Agentic-AI-based-AUtonomous-Cyber-Security-System
```

### Install Required Packages

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run app.py
```

---

## 📦 Technologies Used

### Programming Language
- Python

### Machine Learning
- Scikit-Learn
- Random Forest Classifier

### Data Processing
- Pandas
- NumPy

### Visualization
- Matplotlib

### Frontend
- Streamlit

---

## 🔐 Attack Categories

### 1. Benign Traffic

Normal network communication without malicious behavior.

### 2. FTP Brute Force Attack

Attackers repeatedly attempt different username-password combinations to gain unauthorized access to FTP servers.

Characteristics:
- High login attempts
- Repeated connections
- Small time intervals between requests

### 3. SSH Brute Force Attack

Attackers repeatedly attempt different credentials to access remote systems through SSH.

Characteristics:
- Multiple authentication attempts
- High connection frequency
- Abnormal access patterns

---

## 🌍 Real-World Applications

This project can be applied in:

- Enterprise Network Security
- Intrusion Detection Systems (IDS)
- Security Operations Centers (SOC)
- Educational Cybersecurity Platforms
- Automated Threat Monitoring Systems
- Research and Development Environments

---

## 🔮 Future Enhancements

Future improvements may include:

- Real-time packet monitoring
- Live network traffic integration
- Deep Learning-based detection
- Multi-class attack detection
- Automated firewall integration
- IP blocking mechanisms
- Cloud deployment
- Advanced analytics dashboard
- Threat intelligence integration

---

## 📈 Project Outcomes

- Successfully classified network traffic
- Detected FTP and SSH brute force attacks
- Implemented autonomous decision-making concepts
- Demonstrated practical AI applications in cybersecurity
- Built an interactive monitoring dashboard

---

## 📁 Project Structure

```text
AI-Cybersecurity-Threat-Detection/
│
├── app.py
├── model.py
├── dataset/
│   └── cicids_subset.csv
│
├── models/
│   └── random_forest.pkl
│
├── requirements.txt
├── README.md
│
└── assets/
    └── screenshots/
```

---

## 🎓 Learning Outcomes

Through this project, the following concepts were explored:

- Cybersecurity Fundamentals
- Intrusion Detection Systems
- Machine Learning for Security
- Random Forest Classification
- Network Traffic Analysis
- Agentic AI Concepts
- Streamlit Application Development
- Threat Detection and Response

---

## 👨‍💻 Author

**Priya**  
B.Tech – Computer Science Engineering (AI & ML)

---

## 📜 License

This project is developed for educational, research, and learning purposes.

---

⭐ If you found this project useful, consider giving it a star on GitHub.
