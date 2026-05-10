from selenium.webdriver.common.by import By
from pages.basepage import BasePage
from utils.logger import LogGen

logger = LogGen.loggen()


class LoginPage(BasePage):
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")
    ERROR_MESSAGE = (By.TAG_NAME, "h3")

    def login(self, username="standard_user", password="secret_sauce"):
        logger.info(f'Trying to login with {username}, {password}')
        self.type(self.USERNAME, username)
        self.type(self.PASSWORD, password)
        self.click(self.LOGIN_BTN)

    def read_error_message(self):
        logger.info(f'Trying to display error message')
        return self.get_text(self.ERROR_MESSAGE)