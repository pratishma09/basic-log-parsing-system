import re
from datetime import datetime

PATTERNS = [
    r"failed login",
    r"unauthorized access",
    r"malicious activity detected"
]

def check_line_for_alerts(line):
    for pattern in PATTERNS:
        if re.search(pattern, line, re.IGNORECASE):
            return pattern
    return None

def monitor_logs(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line_number, line in enumerate(file, start=1):
                matched_pattern = check_line_for_alerts(line)
                if matched_pattern:
                    timestamp = extract_or_generate_timestamp(line)
                    alert_message = f"ALERT: {matched_pattern.upper()} DETECTED AT {timestamp}"
                    print(alert_message)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")

def extract_or_generate_timestamp(line):
    timestamp_patterns = [
        r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}",
        r"\d{2}/[A-Za-z]+/\d{4}:\d{2}:\d{2}:\d{2}"
    ]
    for pattern in timestamp_patterns:
        match = re.search(pattern, line)
        if match:
            return match.group()

    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Run using: python system.py logfile.log")
    else:
        log_file = sys.argv[1]
        monitor_logs(log_file)
