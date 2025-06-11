def mitre_mapping(log: str) -> str:
    """
    Maps log messages to MITRE ATT&CK techniques based on specific keywords.

    Parameters:
    log (str): The log message to be analyzed.

    Returns:
    str: The corresponding MITRE ATT&CK technique identifier or "Unknown Technique".
    """

    # Convert the log message to lowercase for case-insensitive matching
    log_lower = log.lower()

    # Check if the log contains the keyword "powershell"
    if "powershell" in log_lower:
        # Return the corresponding MITRE technique for PowerShell usage
        return "T1059: Command and Scripting Interpreter"

    # Check if the log contains the phrase "login failed"
    elif "login failed" in log_lower:
        # Return the corresponding MITRE technique for brute force attacks
        return "T1110: Brute Force"

    # If no known keywords are found, return "Unknown Technique"
    else:
        return "Unknown Technique"
