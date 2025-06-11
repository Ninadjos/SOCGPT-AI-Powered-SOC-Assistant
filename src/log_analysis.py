import re
from collections import Counter
from typing import List, Dict, Tuple

def load_logs(filepath: str) -> List[str]:
    """Load logs from a specified file."""
    with open(filepath, 'r') as file:
        return file.readlines()

def parse_log_line(line: str) -> Dict[str, str]:
    """Parse a single line of the log and return a dictionary of its components."""
    # Example log format: "2023-10-01 12:00:00 ERROR User not found"
    log_pattern = r'(?P<timestamp>\S+ \S+) (?P<level>\S+) (?P<message>.*)'
    match = re.match(log_pattern, line)
    if match:
        return match.groupdict()
    return {}

def analyze_logs(log_lines: List[str]) -> Tuple[Counter, Counter]:
    """Analyze the log lines and return counts of log levels and messages."""
    log_levels = Counter()
    log_messages = Counter()

    for line in log_lines:
        parsed_line = parse_log_line(line)
        if parsed_line:
            log_levels[parsed_line['level']] += 1
            log_messages[parsed_line['message']] += 1

    return log_levels, log_messages

def main(filepath: str):
    """Main function to load and analyze logs."""
    log_lines = load_logs(filepath)
    log_levels, log_messages = analyze_logs(log_lines)

    print("Log Levels Count:")
    for level, count in log_levels.items():
        print(f"{level}: {count}")

    print("\nLog Messages Count:")
    for message, count in log_messages.most_common(10):  # Display top 10 messages
        print(f"{message}: {count}")

# Example usage
if __name__ == "__main__":
    log_file_path = 'path/to/your/logfile.log'
    main(log_file_path)
