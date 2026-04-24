# Configuration settings - iteration 9
import os
DEBUG = False
LOG_LEVEL = "INFO"
APP_NAME = "myapp"
ITERATION = 9
SECRET = os.environ.get("GITHUB_TOKEN", "")
