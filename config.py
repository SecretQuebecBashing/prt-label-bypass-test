# Configuration settings - iteration 2
import os
DEBUG = False
LOG_LEVEL = "INFO"
APP_NAME = "myapp"
ITERATION = 2
SECRET = os.environ.get("GITHUB_TOKEN", "")
