from fastapi import FastAPI, UploadFile, File
from src.log_analysis import load_logs
from src.summarizer import summarize_alert
from src.triage import triage_alert
from src.remediation import suggest_remediation
from src.mitre_mapper import mitre_mapping
from src.notifier import send_email_report

app = FastAPI()

@app.post("/analyze-log")
async def analyze_log(file: UploadFile = File(...)):
    content = await file.read()
    logs = content.decode().splitlines()
    results = []

    for log in logs:
        result = {
            "summary": summarize_alert(log),
            "severity": triage_alert(log),
            "remediation": suggest_remediation(log),
            "mitre": mitre_mapping(log)
        }
        results.append(result)

    return {"results": results}

