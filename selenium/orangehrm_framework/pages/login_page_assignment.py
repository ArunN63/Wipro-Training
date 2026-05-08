from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


from pages.dashboard_page_assignment import DashboardPage


class LoginPage:

    username_input = (By.NAME, "username")
    password_input = (By.NAME, "password")
    login_button = (By.XPATH, "//button[@type='submit']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def enter_username(self, username):
        self.driver.find_element(*self.username_input).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

        self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//h6[text()='Dashboard']")
            )
        )

        return DashboardPage(self.driver)

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        return self.click_login()