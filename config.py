# Configuration settings - iteration 10
import os
DEBUG = False
LOG_LEVEL = "INFO"
APP_NAME = "myapp"
ITERATION = 10
SECRET = os.environ.get("GITHUB_TOKEN", "")
