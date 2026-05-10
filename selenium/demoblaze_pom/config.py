# Configuration file for the project
import os

BASE_URL = "https://www.demoblaze.com/index.html"
IMPLICIT_WAIT = 10
EXPLICIT_WAIT = 20

# Screenshot directory
SCREENSHOTS_DIR = "screenshots"
if not os.path.exists(SCREENSHOTS_DIR):
    os.makedirs(SCREENSHOTS_DIR)

# Logs directory
LOGS_DIR = "logs"
if not os.path.exists(LOGS_DIR):
    os.makedirs(LOGS_DIR)