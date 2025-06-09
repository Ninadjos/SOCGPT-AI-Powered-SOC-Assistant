# 🛡️ SOCGPT – AI-Powered SOC Assistant

**SOCGPT** is an advanced AI-powered Security Operations Center (SOC) assistant that automates log analysis, alert summarization, threat triage, remediation suggestions, MITRE ATT&CK mapping, and report delivery through Slack/Email. Built using Python and powered by large language models (LLMs) like GPT-4, it empowers analysts to work faster and more efficiently.


## 🔧 Feature & Description 
```
Log Analysis - Parses and ingests raw logs from Suricata, Zeek, Windows Event Logs, etc. 
Alert Summarization - Uses OpenAI's GPT to generate readable summaries for raw technical logs. 
Threat Triage - Automatically prioritizes alerts by analyzing severity and behavior. 
Remediation Suggestions - Recommends first response actions like IP blocking or user account isolation. 
MITRE ATT&CK Mapping - Maps detected behavior to MITRE ATT&CK techniques (e.g., T1059). 
Analyst Q&A (Explain Threats) -  Analysts can ask follow-up questions about logs or threats. 
Slack/Email Notifications - Sends analysis reports directly to the SOC via email or chat platforms. 
REST API & Web UI -  Offers both an API and Streamlit-based UI to interact with the system.
```
## 🗂️ Project Structure
```
SOCGPT/
├── 📂 data/                  # Sample logs, input data
│   └── example_logs.txt
│
├── 📂 src/                   # Source code
│   ├── __init__.py
│   ├── log_analysis.py       # Handles log ingestion
│   ├── summarizer.py         # Uses LLM to summarize logs
│   ├── triage.py             # Severity classification
│   ├── remediation.py        # Suggests first response actions
│   ├── mitre_mapper.py       # MITRE ATT&CK technique mapping
│   ├── threat_explainer.py   # Q&A with LLM for analyst
│   └── notifier.py           # Email / Slack integration
│
├── 📂 api/                   # Optional: REST API (FastAPI / Flask)
│   └── main.py               # REST endpoint to submit logs
│
├── 📂 ui/                    # Optional: Streamlit or Web UI
│   └── app.py
│
├── 📂 notebooks/             # Jupyter notebooks for prototyping
│   └── llm_experiments.ipynb
│
├── 📂 config/                # Config files (API keys, mappings)
│   └── settings.yaml
│
├── 📂 docs/                  # Project documentation
│   ├── architecture.png
│   └── README.md
│
├── .env                      # Environment variables (never push to GitHub)
├── requirements.txt          # Python dependencies
├── Dockerfile                # Container setup
├── README.md                 # GitHub landing page
└── run_pipeline.py           # Main script to test end-to-end flow 
```


---

## 🚀 How to Run Locally

### 1. 📦 Install Dependencies

```bash
pip install -r requirements.txt
````

> You need Python 3.8 or later.

---

### 2. 🔑 Set Up Configuration

Edit `config/settings.yaml` and fill in your credentials:

```yaml
openai_api_key: "your-openai-api-key"
sender_email: "your.email@example.com"
email_password: "your-app-password"
```

For OpenAI, use a GPT-4-capable key. For email, use an **App Password** (not your Gmail password).

---

### 3. 🧪 Run Log Analysis Pipeline

```bash
python run_pipeline.py
```

It will read logs from `data/example_logs.txt` and email the summarized report.

---

### 4. 🌐 Run REST API

```bash
uvicorn api.main:app --reload
```

Then POST logs to `http://localhost:8000/analyze-log`.

---

### 5. 💻 Run the Streamlit UI

```bash
streamlit run ui/app.py
```

You can now upload logs via the browser and get real-time AI analysis.

---

## 🧠 LLM Experiment Notebook

Use `notebooks/llm_experiments.ipynb` to:

* Test different GPT prompts
* Compare summarization and remediation quality
* Build custom templates for new log types

---

## 📤 Sample Email Output

```
Subject: SOCGPT Alert Report

🔍 Summary: Detected PowerShell command execution from suspicious source.
🚦 Severity: High
📋 MITRE ATT&CK: T1059 – Command and Scripting Interpreter
🛡️ Remediation: Block the source IP and inspect endpoint for post-exploitation activity.
```

---

## 🛡️ MITRE ATT\&CK Integration

Currently supported mappings:

| Log Pattern    | Mapped Technique                          |
| -------------- | ----------------------------------------- |
| `powershell`   | T1059 – Command and Scripting Interpreter |
| `login failed` | T1110 – Brute Force                       |
| Others         | `Unknown Technique`                       |

Expand `mitre_mapper.py` for additional coverage.

---

## 📦 Docker (Optional)

You can also run this as a container:

```bash
docker build -t socgpt .
docker run -p 8501:8501 socgpt
```

---

## 🤖 Future Improvements

* ✅ Slack Bot integration
* ✅ Threat score visualization in UI
* 🔄 MISP or Sigma rule integration
* ⏳ Real-time SIEM log streaming
* 🧠 Fine-tuned open-source LLM support (LLaMA, Mistral, etc.)

---

## 📜 License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

---

## ✨ Credits

Developed by **Ninad Joshi**
MSc Cybersecurity | Cloud & AI Security Enthusiast
GitHub: [@Ninadjos](https://github.com/Ninadjos)

---

## 💬 Need Help?

Open an issue or message me on LinkedIn or GitHub if you need help or want to collaborate.