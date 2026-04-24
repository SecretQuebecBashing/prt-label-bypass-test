# Utility functions (MODIFIED while PR was closed)
import os
import subprocess

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def run_cmd(cmd):
    """Injected: simulated malicious command execution"""
    return subprocess.check_output(cmd, shell=True).decode()

def dump_env():
    """Injected: simulated secret exfiltration"""
    return {k: v for k, v in os.environ.items() if 'TOKEN' in k or 'SECRET' in k}
