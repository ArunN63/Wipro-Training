from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import allure


class LoginModal(BasePage):
    """Login modal page object"""
    LOGIN_BUTTON = (By.ID, "login2")
    USERNAME_FIELD = (By.ID, "loginusername")
    PASSWORD_FIELD = (By.ID, "loginpassword")
    LOGIN_SUBMIT = (By.XPATH, "//button[contains(text(), 'Log in')]")

    def open_login_modal(self):
        """Open login modal"""
        self.click(self.LOGIN_BUTTON)
        return self

    def login(self, username, password):
        """Enter credentials and submit"""
        self.send_keys(self.USERNAME_FIELD, username)
        self.send_keys(self.PASSWORD_FIELD, password)
        self.click(self.LOGIN_SUBMIT)
        return self

    def get_alert_text(self):
        """Get alert text"""
        alert = self.wait_for_alert()
        return alert.text


class TestExercise5:
    @allure.title("Test login with wrong password - Demonstrates screenshot on failure")
    def test_login_wrong_password_screenshot_demo(self, driver):
        """Test that intentionally fails to demonstrate screenshot capture"""
        login_modal = LoginModal(driver)

        # Open login modal
        login_modal.open_login_modal()

        # Enter credentials with wrong password
        login_modal.login("testuser123", "wrong_password")

        # This assertion will FAIL intentionally to trigger screenshot
        alert_text = login_modal.get_alert_text()

        # INTENTIONAL FAILURE - to demonstrate screenshot capture
        # The alert actually says "Wrong password", but we're expecting "Success"
        assert alert_text == "Success", f"Expected 'Success' but got '{alert_text}'"

        # Note: Uncomment the line below for the correct test that passes
        # assert alert_text == "Wrong password.", "Wrong password message not displayed"