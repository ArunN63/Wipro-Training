from selenium.webdriver.common.by import By


class AdminPage:

    admin_menu = (By.XPATH, "//span[text()='Admin']")

    username_box = (
        By.XPATH,
        "(//input[@class='oxd-input oxd-input--active'])[2]"
    )

    search_btn = (
        By.XPATH,
        "//button[contains(.,'Search')]"
    )

    records = (
        By.XPATH,
        "//div[@class='oxd-table-card']"
    )

    def __init__(self, driver):

        self.driver = driver

    def click_admin(self):

        self.driver.find_element(*self.admin_menu).click()

    def enter_username(self, uname):

        self.driver.find_element(*self.username_box).send_keys(uname)

    def click_search(self):

        self.driver.find_element(*self.search_btn).click()

    def get_records(self):

        return self.driver.find_elements(*self.records)
