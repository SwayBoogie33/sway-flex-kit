# sway-flex-kit
Hands-on cybersecurity scripts I'm building to sharpen my skills. This is my personal toolkit.
# Flex Kit – Sway's Cybersecurity Scripts

Welcome to my Flex Kit — a growing collection of Python scripts and tools I’m building on my journey into cybersecurity.

## Script: Failed Login Parser

**File:** `failed_logins.py`

This script reads a system log file and parses it to identify failed login attempts.  
It extracts the username and IP address from each failure and prints it in a clean, readable format.

### What it shows:
- Log file parsing
- Conditional logic
- String manipulation
- Basic automation

### Why I built it:
This is part of my personal toolkit to build hands-on skills while preparing for my Security+ certification and growing my cyber career.

---

**More scripts coming soon.**
---

## Script: IP Blacklist Filter

**File:** `ip_blacklist_filter.py`

This script scans a system log file and tracks failed login attempts by IP address.  
If any IP fails to log in 3 or more times, it is flagged as suspicious.

### What it shows:
- Use of dictionaries for counting
- Log parsing and string operations
- Threshold logic for detection
- Real-world application for brute-force or intrusion attempts

### Why I built it:
To practice log analysis and IP tracking—key tasks in SOC and analyst roles.  
This builds on my first parser and strengthens my understanding of automation and threat detection.
