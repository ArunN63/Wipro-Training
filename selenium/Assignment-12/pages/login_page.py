from selenium.webdriver.common.by import By


class LoginPage:

    username = (By.NAME, "username")
    password = (By.NAME, "password")
    login_btn = (By.XPATH, "//button[@type='submit']")
    invalid_msg = (
        By.XPATH,
        "//p[contains(text(),'Invalid credentials')]"
    )

    def __init__(self, driver):
        self.driver = driver

    def open_url(self):

        self.driver.get(
            "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        )

    def enter_username(self, uname):

        self.driver.find_element(*self.username).send_keys(uname)

    def enter_password(self, pwd):

        self.driver.find_element(*self.password).send_keys(pwd)

    def click_login(self):

        self.driver.find_element(*self.login_btn).click()

    def get_invalid_message(self):

        return self.driver.find_element(*self.invalid_msg).text