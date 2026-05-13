from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class DashboardPage(BasePage):
    # Locators
    DASHBOARD_TITLE = (By.XPATH, "//h6[text()='Dashboard']")
    PIM_MODULE = (By.XPATH, "//span[text()='PIM']")
    ADMIN_MODULE = (By.XPATH, "//span[text()='Admin']")
    LEAVE_MODULE = (By.XPATH, "//span[text()='Leave']")
    MYINFO_MODULE = (By.XPATH, "//span[text()='My Info']")
    USER_DROPDOWN = (By.CLASS_NAME, "oxd-userdropdown-tab")

    def get_dashboard_title(self):
        """Get dashboard title text"""
        return self.get_text(self.DASHBOARD_TITLE)

    def navigate_to_pim(self):
        """Navigate to PIM module"""
        self.click(self.PIM_MODULE)
        from pages.pim_page import PIMPage
        return PIMPage(self.driver)

    def navigate_to_admin(self):
        """Navigate to Admin module"""
        self.click(self.ADMIN_MODULE)
        from pages.admin_page import AdminPage
        return AdminPage(self.driver)

    def navigate_to_leave(self):
        """Navigate to Leave module"""
        self.click(self.LEAVE_MODULE)
        from pages.leave_page import LeavePage
        return LeavePage(self.driver)

    def navigate_to_myinfo(self):
        """Navigate to My Info module"""
        self.click(self.MYINFO_MODULE)
        from pages.myinfo_page import MyInfoPage
        return MyInfoPage(self.driver)

    def is_dashboard_displayed(self):
        """Check if dashboard is displayed"""
        return self.find(self.DASHBOARD_TITLE).is_displayed()