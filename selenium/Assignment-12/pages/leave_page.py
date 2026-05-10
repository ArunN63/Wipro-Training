from selenium.webdriver.common.by import By


class LeavePage:

    leave_menu = (By.XPATH, "//span[text()='Leave']")

    apply_menu = (
        By.XPATH,
        "//a[contains(text(),'Apply')]"
    )

    def __init__(self, driver):

        self.driver = driver

    def click_leave(self):

        self.driver.find_element(*self.leave_menu).click()

    def click_apply(self):

        self.driver.find_element(*self.apply_menu).click()