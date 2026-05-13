from pytest_bdd import scenarios, given, when, then, parsers
from pages.login_page import LoginPage
from utilities.config import VALID_USERNAME, VALID_PASSWORD, INVALID_PASSWORD

# Change this line:
# scenarios('../features/login.feature')
# To:
scenarios('features/features/login.feature')  # If features is inside features

# OR better yet:
import os
feature_file = os.path.join('features', 'features', 'login.feature')
scenarios(feature_file)