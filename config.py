# Configuration settings - iteration 5
import os
DEBUG = False
LOG_LEVEL = "INFO"
APP_NAME = "myapp"
ITERATION = 5
SECRET = os.environ.get("GITHUB_TOKEN", "")
