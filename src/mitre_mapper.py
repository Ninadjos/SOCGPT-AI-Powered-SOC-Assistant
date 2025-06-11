def mitre_mapping(log: str) -> str:
    if "powershell" in log.lower():
        return "T1059: Command and Scripting Interpreter"
    elif "login failed" in log.lower():
        return "T1110: Brute Force"
    else:
        return "Unknown Technique"