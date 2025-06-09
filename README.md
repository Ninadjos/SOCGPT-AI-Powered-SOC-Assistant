SOCGPT is an AI-powered tool for Security Operations Centers. It automates log analysis, triage, and remediation using LLMs.

## Features
- 🔍 Log Analysis from Zeek, Suricata, etc.
- ⚠️ Alert Summarization with LLM
- 🚦 Threat Triage
- 🛡️ Remediation Suggestion
- 📋 MITRE ATT&CK Mapping
- 📤 Slack/Email Reporting
- 💡 LLM Q&A for Analysts

## How to Run
```bash
pip install -r requirements.txt
python run_pipeline.py
```

## API Usage
```bash
uvicorn api.main:app --reload
```

## UI
```bash
streamlit run ui/app.py
```