from src.log_analysis import load_logs
from src.summarizer import summarize_alert
from src.triage import triage_alert
from src.remediation import suggest_remediation
from src.mitre_mapper import mitre_mapping
from src.notifier import send_email_report

EMAIL_TO = "analyst@example.com"


def run_pipeline(log_path: str, email: str):
    logs = load_logs(log_path)
    for log in logs:
        summary = summarize_alert(log)
        severity = triage_alert(log)
        remediation = suggest_remediation(log)
        mitre = mitre_mapping(log)

        report = f"""
        🔍 Summary: {summary}
        🚦 Severity: {severity}
        📋 MITRE ATT&CK: {mitre}
        🛡️ Remediation: {remediation}
        """
        send_email_report("SOCGPT Alert Report", report, email)


if __name__ == "__main__":
    run_pipeline("data/example_logs.txt", EMAIL_TO)
