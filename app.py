import os
import subprocess
import hashlib

# Vulnerability 1: Hardcoded Password
ADMIN_PASSWORD = "SuperSecretPassword123!"

def run_command(user_input):
    # Vulnerability 2: Command Injection
    # Passing unsanitized input directly to the shell
    subprocess.call(user_input, shell=True)

def hash_password(password):
    # Vulnerability 3: Weak Hashing Algorithm (MD5)
    return hashlib.md5(password.encode()).hexdigest()

if __name__ == "__main__":
    print("Application started.")
    # Simulating a user input that could be malicious
    user_cmd = input("Enter a command to run: ")
    run_command(user_cmd)
