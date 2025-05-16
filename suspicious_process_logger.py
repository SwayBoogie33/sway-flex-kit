import psutil

# List of suspicious process names
suspicious_processes = ["keylogger", "malware", "rat", "spyware", "bitcoinminer"]

# Open a log file
with open("process_log.txt", "w") as log:
    log.write("Suspicious Process Log:\n\n")

    # Loop through all running processes
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            process_name = proc.info['name'].lower()
            if any(suspicious in process_name for suspicious in suspicious_processes):
                alert = f"Suspicious process found: {process_name} (PID: {proc.info['pid']})"
                print(alert)
                log.write(alert + "\n")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue

print("\nProcess scan complete.")