from selenium.webdriver.common.by import By


class SideMenuComponent:

    admin_menu = (By.XPATH, "//span[text()='Admin']")
    pim_menu = (By.XPATH, "//span[text()='PIM']")
    leave_menu = (By.XPATH, "//span[text()='Leave']")

    def __init__(self, driver):
        self.driver = driver

    def open_admin(self):
        self.driver.find_element(*self.admin_menu).click()

    def open_pim(self):
        self.driver.find_element(*self.pim_menu).click()

    def open_leave(self):
        self.driver.find_element(*self.leave_menu).click()