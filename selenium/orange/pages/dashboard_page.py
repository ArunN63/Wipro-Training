from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.pim_page import PIMPage
from pages.admin_page import AdminPage
from pages.leave_page import LeavePage
from pages.myinfo_page import MyInfoPage


class DashboardPage(BasePage):
    # Locators
    DASHBOARD_TITLE = (By.XPATH, "//h6[text()='Dashboard']")
    PIM_MODULE = (By.XPATH, "//span[text()='PIM']")
    ADMIN_MODULE = (By.XPATH, "//span[text()='Admin']")
    LEAVE_MODULE = (By.XPATH, "//span[text()='Leave']")
    MYINFO_MODULE = (By.XPATH, "//span[text()='My Info']")
    TIME_MODULE = (By.XPATH, "//span[text()='Time']")
    RECRUITMENT_MODULE = (By.XPATH, "//span[text()='Recruitment']")
    USER_DROPDOWN = (By.CLASS_NAME, "oxd-userdropdown-tab")
    LOGOUT_BUTTON = (By.XPATH, "//a[contains(text(), 'Logout')]")
    WELCOME_MESSAGE = (By.XPATH, "//p[@class='oxd-userdropdown-name']")

    def get_dashboard_title(self):
        """Get dashboard title text"""
        return self.get_text(self.DASHBOARD_TITLE)

    def is_dashboard_displayed(self):
        """Check if dashboard is displayed"""
        try:
            return self.find(self.DASHBOARD_TITLE).is_displayed()
        except:
            return False

    def navigate_to_pim(self):
        """Navigate to PIM module"""
        self.click(self.PIM_MODULE)
        return PIMPage(self.driver)

    def navigate_to_admin(self):
        """Navigate to Admin module"""
        self.click(self.ADMIN_MODULE)
        return AdminPage(self.driver)

    def navigate_to_leave(self):
        """Navigate to Leave module"""
        self.click(self.LEAVE_MODULE)
        return LeavePage(self.driver)

    def navigate_to_myinfo(self):
        """Navigate to My Info module"""
        self.click(self.MYINFO_MODULE)
        return MyInfoPage(self.driver)

    def get_welcome_text(self):
        """Get welcome message text"""
        return self.get_text(self.WELCOME_MESSAGE)

    def logout(self):
        """Logout from application"""
        self.click(self.USER_DROPDOWN)
        self.click(self.LOGOUT_BUTTON)
        from pages.login_page import LoginPage
        return LoginPage(self.driver)