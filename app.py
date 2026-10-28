import os
import subprocess
import hashlib

# Fix 1: Use environment variables instead of hardcoding
ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD")

def run_command(user_input):
    # Fix 2: Avoid shell=True and sanitize input
    if not user_input.isalnum():
        print("Invalid input detected.")
        return
    subprocess.call(["echo", user_input]) 

def hash_password(password):
    # Fix 3: Use a strong hashing algorithm (SHA-256)
    return hashlib.sha256(password.encode()).hexdigest()

if __name__ == "__main__":
    print("Application started.")
    user_cmd = input("Enter a command to run: ")
    run_command(user_cmd)
