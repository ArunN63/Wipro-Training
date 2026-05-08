from selenium.webdriver.common.by import By

from pages.side_menu_component_assignment import SideMenuComponent


class DashboardPage:

    dashboard_heading = (By.XPATH, "//h6[text()='Dashboard']")

    def __init__(self, driver):
        self.driver = driver
        self.side_menu = SideMenuComponent(driver)

    def is_dashboard_displayed(self):
        return self.driver.find_element(*self.dashboard_heading).is_displayed()