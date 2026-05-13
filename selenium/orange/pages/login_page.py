from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.dashboard_page import DashboardPage


class LoginPage(BasePage):
    # Locators
    USERNAME_INPUT = (By.NAME, "username")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")
    ERROR_MESSAGE = (By.XPATH, "//p[contains(@class, 'oxd-alert-content-text')]")
    ORANGEHRM_LOGO = (By.XPATH, "//img[@alt='company-branding']")
    RESET_PASSWORD_LINK = (By.XPATH, "//p[contains(text(), 'Forgot')]")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    def login(self, username, password):
        """Login with username and password"""
        self.logger.info(f"Logging in with username: {username}")
        self.send_keys(self.USERNAME_INPUT, username)
        self.send_keys(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)
        return DashboardPage(self.driver)

    def login_invalid(self, username, password):
        """Login with invalid credentials"""
        self.logger.info(f"Attempting login with username: {username}")
        self.send_keys(self.USERNAME_INPUT, username)
        self.send_keys(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)
        return self

    def get_error_message(self):
        """Get error message text"""
        return self.get_text(self.ERROR_MESSAGE)

    def is_login_page(self):
        """Verify if on login page"""
        return "login" in self.get_current_url()

    def clear_credentials(self):
        """Clear username and password fields"""
        self.find(self.USERNAME_INPUT).clear()
        self.find(self.PASSWORD_INPUT).clear()
        return self