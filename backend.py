from flask import Flask, render_template, jsonify
import csv, os
from datetime import datetime
from relatime_detection import detect_network_flow_with_features
from AgenticAI import agent

app = Flask(__name__)

# ==============================
# CSV log for previous records
# ==============================
LOG_FILE = "traffic_logs.csv"

# Create CSV with headers if not exists
if not os.path.exists(LOG_FILE):
    with open(LOG_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            "Timestamp", "Flow_ID", "Prediction", "Attack_Name",
            "Top_Features", "Agent_Decision", "Agent_Actions"
        ])

# ==============================
# Helper: Log detection
# ==============================
def log_detection(flow_id, prediction, attack_name, top_features, agent_decision, agent_actions):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            timestamp,
            flow_id,
            prediction,
            attack_name,
            ", ".join(top_features),
            agent_decision,
            ", ".join(agent_actions)
        ])

# ==============================
# Helper: Get last 50 records
# ==============================
def get_last_records():
    records = []
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            reader = list(csv.DictReader(f))
            for row in reader[-50:]:  # last 50 records
                records.append(row)
    return records

# ==============================
# Home route
# ==============================
@app.route('/')
def home():
    return render_template("frontend.html")  # your dashboard HTML file

# ==============================
# Endpoint: Run one detection
# ==============================
@app.route('/latest', methods=['GET'])
def latest_detection():
    # Detect one flow
    prediction, attack_name, top_features = detect_network_flow_with_features()
    flow_id = datetime.now().strftime("%H%M%S%f")  # unique flow ID

    # Agent decision
    agent_decision, agent_actions = agent.take_action(prediction, flow_id)

    # Log the detection
    log_detection(flow_id, prediction, attack_name, top_features, agent_decision, agent_actions)

    # Get last 50 records for dashboard
    records = get_last_records()
    total = len(records)
    attacks = sum(1 for r in records if r["Prediction"] == "Attack")
    normal = total - attacks

    return jsonify({
        "prediction": prediction,
        "attack_name": attack_name,
        "top_features": top_features,
        "agent_decision": agent_decision,
        "agent_actions": agent_actions,
        "total": total,
        "attacks": attacks,
        "normal": normal,
        "records": records
    })

# ==============================
# Endpoint: Get stats for page load
# ==============================
@app.route('/stats', methods=['GET'])
def stats():
    records = get_last_records()
    total = len(records)
    attacks = sum(1 for r in records if r["Prediction"] == "Attack")
    normal = total - attacks
    return jsonify({
        "total": total,
        "attacks": attacks,
        "normal": normal,
        "records": records
    })

# ==============================
# Run Flask server
# ==============================
if __name__ == '__main__':
    app.run(debug=True)