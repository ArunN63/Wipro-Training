from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.dashboard_page import DashboardPage
from utilities.config import BASE_URL


class LoginPage(BasePage):
    # Locators
    USERNAME_INPUT = (By.NAME, "username")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")
    ERROR_MESSAGE = (By.XPATH, "//p[contains(@class, 'alert')]")
    ORANGEHRM_LOGO = (By.XPATH, "//img[@alt='company-branding']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(BASE_URL)

    def login(self, username, password):
        """Login with username and password"""
        self.logger.info(f"Logging in with username: {username}")
        self.send_keys(self.USERNAME_INPUT, username)
        self.send_keys(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

        from pages.dashboard_page import DashboardPage
        return DashboardPage(self.driver)

    def login_invalid(self, username, password):
        """Login with invalid credentials"""
        self.logger.info(f"Attempting login with invalid password")
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