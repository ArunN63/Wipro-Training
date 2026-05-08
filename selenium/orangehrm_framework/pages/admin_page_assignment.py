from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.side_menu_component_assignment import SideMenuComponent

class AdminPage:
    usernames_list = (
        By.XPATH,
        "//div[@role='row']//div[2]"
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.side_menu = SideMenuComponent(driver)

    def is_user_present(self, expected_username):

        self.wait.until(
            EC.visibility_of_all_elements_located(self.usernames_list)
        )
        usernames = self.driver.find_elements(*self.usernames_list)

        for user in usernames:
            if user.text == expected_username:
                return True

        return False