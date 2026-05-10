from selenium.webdriver.common.by import By


class ProfilePage:

    myinfo_menu = (
        By.XPATH,
        "//span[text()='My Info']"
    )

    nickname_box = (
        By.XPATH,
        "(//input[@class='oxd-input oxd-input--active'])[3]"
    )

    upload_btn = (
        By.XPATH,
        "//input[@type='file']"
    )

    save_btn = (
        By.XPATH,
        "//button[@type='submit']"
    )

    def __init__(self, driver):

        self.driver = driver

    def click_myinfo(self):

        self.driver.find_element(*self.myinfo_menu).click()

    def update_nickname(self, nickname):

        box = self.driver.find_element(*self.nickname_box)

        box.clear()
        box.send_keys(nickname)

    def upload_photo(self, filepath):
        upload = self.driver.find_element(
            *self.upload_btn
        )

        self.driver.execute_script(
            "arguments[0].style.display='block';",
            upload
        )

        upload.send_keys(filepath)

    def click_save(self):

        self.driver.find_element(*self.save_btn).click()