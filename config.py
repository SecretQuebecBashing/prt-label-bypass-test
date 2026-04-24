# Configuration settings - iteration 3
import os
DEBUG = False
LOG_LEVEL = "INFO"
APP_NAME = "myapp"
ITERATION = 3
SECRET = os.environ.get("GITHUB_TOKEN", "")
