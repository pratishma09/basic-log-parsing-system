# basic-log-parsing-system
A function that reads a log file and identifies if any error messages or suspicious patterns (e.g., “failed login”, “unauthorized access”, “malicious activity detected”) appear. If such a pattern is detected, the system should generate a simple alert (print a message or log it).

---
## 🚀 Project Overview

SystemMonitor simulates a basic SIEM-like functionality by:
- Reading log files line by line
- Searching for suspicious patterns using regular expressions
- Searching for date format or using current timestamp for alert messages
- Printing real-time alerts with timestamps when a match with suspicious pattern is detected
---

## Steps to run the code:
1. Clone the repo using: git clone https://github.com/pratishma09/basic-log-parsing-system.git
2. cd basic-log-parsing-system
3. Run python system.py logfile.log

## Assumptions:
1. Uses the patterns: “failed login”, “unauthorized access”, “malicious activity detected”.
2. Logs are plain text files, .txt or .log with timestamps.

## Limitations:
1. Does not parse structured log formats
2. Does not persist or store alerts

## References:
1. Sample log file: https://zenduty.com/blog/log-file/
2. https://signoz.io/guides/log-parsing/