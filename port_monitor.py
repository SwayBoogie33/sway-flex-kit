# port_monitor.py

# Simulated list of open ports
open_ports = [21, 22, 23, 25, 80, 443, 445, 3389]

# Known risky ports
risky_ports = {
    23: "Telnet (Unencrypted)",
    445: "SMB (Often exploited)",
    3389: "RDP (Remote Desktop)"
}

# Scan ports and report status
print("Scanning...\n")

for port in open_ports:
    if port in risky_ports:
        print(f"Port {port}: RISKY - {risky_ports[port]}")
    else:
        print(f"Port {port}: Safe")

print("\nScan complete.")
