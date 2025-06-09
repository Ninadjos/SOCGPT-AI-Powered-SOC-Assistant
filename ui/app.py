import streamlit as st
from src.log_analysis import load_logs
from src.summarizer import summarize_alert
from src.triage import triage_alert
from src.remediation import suggest_remediation
from src.mitre_mapper import mitre_mapping

st.title("SOCGPT: AI-Powered SOC Assistant")

uploaded_file = st.file_uploader("Upload a log file")

if uploaded_file:
    logs = uploaded_file.read().decode().splitlines()
    for log in logs:
        st.markdown(f"### Log: {log}")
        st.write(f"🔍 Summary: {summarize_alert(log)}")
        st.write(f"🚦 Severity: {triage_alert(log)}")
        st.write(f"📋 MITRE ATT&CK: {mitre_mapping(log)}")
        st.write(f"🛡️ Remediation: {suggest_remediation(log)}")