# Configuration settings - iteration 1
import os
DEBUG = False
LOG_LEVEL = "INFO"
APP_NAME = "myapp"
ITERATION = 1
SECRET = os.environ.get("GITHUB_TOKEN", "")
