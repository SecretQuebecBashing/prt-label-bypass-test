# Configuration settings - iteration 4
import os
DEBUG = False
LOG_LEVEL = "INFO"
APP_NAME = "myapp"
ITERATION = 4
SECRET = os.environ.get("GITHUB_TOKEN", "")
