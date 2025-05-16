# file_integrity_checker.py

import hashlib

# Path to the file you want to check
file_path = "important_file.txt"

# Known good SHA256 hash (pretend this is what the file should be)
known_hash = "a42f4141d0740647b7f889eb5f735ab7dd9b0a84cc29d901951961af57dbbfb5"

# Read the file and calculate its SHA256 hash
with open(file_path, "rb") as f:
    file_data = f.read()
    current_hash = hashlib.sha256(file_data).hexdigest()

# Compare hashes and print result
print(f"Known hash:   {known_hash}")
print(f"Current hash: {current_hash}\n")

if current_hash == known_hash:
    print("✅ File is intact. No changes detected.")
else:
    print("⚠️  ALERT: File has been modified!")