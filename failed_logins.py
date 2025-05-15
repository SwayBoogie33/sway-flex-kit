
# failed_logins.py

# Step 1 - Open the log file
with open("logfile.txt", "r") as file:
    lines = file.readlines()

# Step 2 - Loop through each line and look for "LOGIN FAIL"
for line in lines:
    if "LOGIN FAIL" in line:
        # Step 3 - Extract username and IP from the line
        parts = line.split()
        user = parts[4].split("=")[1]
        ip = parts[5].split("=")[1]

        # Step 4 - Print failed login info
        print(f"FAILED LOGIN - User: {user}, IP: {ip}")
