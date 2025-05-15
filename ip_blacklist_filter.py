# ip_blacklist_filter.py

# Open the log file
with open("logfile.txt", "r") as file:
    lines = file.readlines()

# Dictionary to count failed login attempts by IP
ip_counts = {}

# Go through each line and look for failed logins
for line in lines:
    if "LOGIN FAIL" in line:
        parts = line.split()
        ip = parts[-1].split("=")[-1]

        if ip in ip_counts:
            ip_counts[ip] += 1
        else:
            ip_counts[ip] = 1

# Print suspicious IPs with 3 or more failed attempts
print("Suspicious IPs:")
for ip, count in ip_counts.items():
    if count >= 3:
        print(f"{ip} - {count} failed attempts")

print("Scan complete.")
