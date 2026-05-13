import os

# Application URLs
BASE_URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
DASHBOARD_URL = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"

# Credentials
VALID_USERNAME = "Admin"
VALID_PASSWORD = "admin123"
INVALID_PASSWORD = "wrongpassword"

# Wait times
IMPLICIT_WAIT = 10
EXPLICIT_WAIT = 20

# Directories
SCREENSHOTS_DIR = "screenshots"
DOWNLOADS_DIR = "downloads"
UPLOADS_DIR = "uploads"

# Create directories if they don't exist
for directory in [SCREENSHOTS_DIR, DOWNLOADS_DIR, UPLOADS_DIR]:
    if not os.path.exists(directory):
        os.makedirs(directory)