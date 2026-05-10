from selenium.webdriver.common.by import By


class DashboardPage:

    def __init__(self, driver):
        self.driver = driver

    dashboard_text = (
        By.XPATH,
        "//h6[text()='Dashboard']"
    )

    def verify_dashboard(self):

        return self.driver.find_element(
            *self.dashboard_text
        ).is_displayed()