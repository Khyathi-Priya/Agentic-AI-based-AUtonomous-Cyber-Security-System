import streamlit as st
import pandas as pd
import time
from relatime_detection import detect_network_flow
from AgenticAI import agent

# ==============================
# Page Config
# ==============================
st.set_page_config(page_title="AI IDS Live Dashboard", layout="wide")
st.title("🔐 AI Threat Detection System ")

# ==============================
# Session State Initialization
# ==============================
if "records" not in st.session_state:
    st.session_state.records = []

if "total_normal" not in st.session_state:
    st.session_state.total_normal = 0

if "total_attack" not in st.session_state:
    st.session_state.total_attack = 0

if "total_traffic" not in st.session_state:
    st.session_state.total_traffic = 0

if "running" not in st.session_state:
    st.session_state.running = False

# ==============================
# Control Buttons
# ==============================
colA, colB = st.columns(2)

if colA.button("▶ Start Live Detection"):
    st.session_state.running = True

if colB.button("⏹ Stop"):
    st.session_state.running = False

st.divider()

# ==============================
# Live Detection Logic
# ==============================
if st.session_state.running:

    flow_id, prediction, attack_type, attack_name, top_features = detect_network_flow()

    decision, actions = agent.take_action(prediction, flow_id)

    st.session_state.total_traffic += 1

    if prediction == "Normal":
        st.session_state.total_normal += 1
    else:
        st.session_state.total_attack += 1

    record = {
        "Flow ID": flow_id,
        "Attack Type": attack_type,
        "Attack Name": attack_name,
        "Top Features": ", ".join(top_features),
        "Prediction": prediction,
        "Agent Decision": decision,
        "Agent Actions": ", ".join(actions)
    }

    st.session_state.records.append(record)

# ==============================
# Metrics Section
# ==============================
col1, col2, col3 = st.columns(3)

col1.metric("Total Traffic", st.session_state.total_traffic)
col2.metric("Normal Traffic", st.session_state.total_normal)
col3.metric("Attack Traffic", st.session_state.total_attack)

st.divider()

# ==============================
# Latest Detection Status
# ==============================
if st.session_state.records:
    latest = st.session_state.records[-1]

    st.subheader("🔍 Latest Traffic Status")

    if latest["Prediction"] == "Attack":
        st.error(f"🚨 ATTACK DETECTED: {latest['Attack Name']}")
    else:
        st.success("✅ Normal Traffic")

    st.write("Agent Decision:", latest["Agent Decision"])
    st.write("Agent Actions:", latest["Agent Actions"])
    st.write("Top Features:", latest["Top Features"])

st.divider()

# ==============================
# Records Table
# ==============================
st.subheader("📋 Detection Records")

if st.session_state.records:
    df_records = pd.DataFrame(st.session_state.records)
    st.dataframe(df_records, use_container_width=True)

# ==============================
# Auto Refresh (Every 2 seconds)
# ==============================
if st.session_state.running:
    time.sleep(2)
    st.rerun()