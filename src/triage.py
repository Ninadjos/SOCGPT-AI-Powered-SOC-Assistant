def triage_alert(log: str) -> str:
    if "powershell" in log.lower():
        return "High"
    elif "login failed" in log.lower():
        return "Medium"
    else:
        return "Low"