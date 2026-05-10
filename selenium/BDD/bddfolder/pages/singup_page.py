import allure

from locators.signup_locators import SignupLocators
from utils.logger import LogGen
from utils.screenshot_util import ScreenshotUtil
from utils.waits import WaitUtils

logger = LogGen.loggen()

class SignupPage:
    def __init__(self, driver):
        self.driver = driver

    def click_signup_menu(self):
        logger.info("Clicking signup Menu")
        WaitUtils.wait_for_element_clickable(self.driver, SignupLocators.SIGNUP_MENU).click()

    def enter_username(self, username):
        logger.info(
            f"Entering Username : {username}"
        )
        element = WaitUtils.wait_for_element_visible(
            self.driver,
            SignupLocators.USERNAME
        )
        element.clear()
        element.send_keys(username)

    def enter_password(self, password):
        logger.info("Entering Password")
        element = WaitUtils.wait_for_element_visible(
            self.driver,
            SignupLocators.PASSWORD
        )
        element.clear()
        element.send_keys(password)

    def click_signup_button(self):
        logger.info("Clicking Signup Button")
        WaitUtils.wait_for_element_clickable(self.driver,SignupLocators.SIGNUP_BUTTON ).click()



    def verify_successful_signup(self):
        logger.info(
            "Verifying Signup Alert"
        )
        alert = WaitUtils.wait_for_alert(self.driver)
        alert_text = alert.text
        logger.info( f"Alert Message : {alert_text}"    )
        ScreenshotUtil.capture_screenshot(self.driver,"signup_alert")
        allure.attach(
            self.driver.get_screenshot_as_png(),
            name="Signup Alert Screenshot",
            attachment_type=allure.attachment_type.PNG
        )
        assert alert_text == 'Sign up successful', 'Signup failed'