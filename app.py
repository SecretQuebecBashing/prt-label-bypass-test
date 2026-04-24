# MODIFIED: This content was changed while the PR was closed
# In a real attack, this could be malicious code injection
import logging
import os
import subprocess

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def hello():
    logger.info("hello() called")
    # INJECTED: Simulated malicious payload
    logger.info(f"SECRET_TOKEN={os.environ.get('SECRET_TOKEN', 'not-set')}")
    return "Hello, World! (modified)"

def exfiltrate():
    """Simulated malicious function added during close/reopen bypass"""
    env_dump = {k: v for k, v in os.environ.items() if 'TOKEN' in k or 'SECRET' in k}
    logger.warning(f"Exfil simulation: {env_dump}")
    return env_dump

if __name__ == "__main__":
    print(hello())
