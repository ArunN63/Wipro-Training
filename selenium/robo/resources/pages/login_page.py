import sys
import os
from typing import cast

from SeleniumLibrary import SeleniumLibrary
from selenium.common import TimeoutException
from selenium.webdriver.common.alert import Alert

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../..")
    )
)

from robot.api.deco import keyword
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from robot.libraries.BuiltIn import BuiltIn

from resources.locators.login_locators import (
    LOGIN_LINK,
    USERNAME_TEXTBOX,
    PASSWORD_TEXTBOX,
    LOGIN_BUTTON,
    WELCOME_USER
)

from resources.variables.config import config

from resources.variables.testdata import (
    VALID_USERNAME,
    VALID_PASSWORD, INVALID_USERNAME, INVALID_PASSWORD
)


class LoginPage:

    @property
    def selenium(self):
        return cast(
            SeleniumLibrary,
            BuiltIn().get_library_instance(
                "SeleniumLibrary"
            )
        )

    @keyword
    def launch_demoblaze_application(self):
        self.selenium.open_browser(
            config.base_url,
            browser=config.browser
        )
        self.selenium.maximize_browser_window()
        self.selenium.set_selenium_implicit_wait(
            config.implicit_wait
        )

    @keyword
    def click_login_link(self):
        self.selenium.click_element(
            LOGIN_LINK
        )

    @keyword
    def enter_username(self):
        self.selenium.input_text(
            USERNAME_TEXTBOX,
            VALID_USERNAME
        )

    @keyword
    def enter_password(self):
        self.selenium.input_text(
            PASSWORD_TEXTBOX,
            VALID_PASSWORD
        )

    @keyword
    def click_signin_button(self):
        self.selenium.click_button(
            LOGIN_BUTTON
        )

    @keyword
    def verify_successful_login(self):
        WebDriverWait(
            self.selenium.driver,
            10
        ).until(
            EC.visibility_of_element_located(
                (By.ID, "nameofuser")
            )
        )
        welcome_text = self.selenium.get_text(
            WELCOME_USER
        )
        print(welcome_text)
        assert "Welcome" in welcome_text

    # ================INVALID=====================

    @keyword
    def enter_invalid_login_username(self):
        self.selenium.input_text(
            USERNAME_TEXTBOX,
            INVALID_USERNAME
        )

    @keyword
    def enter_invalid_login_password(self):
        self.selenium.input_text(
            PASSWORD_TEXTBOX,
            INVALID_PASSWORD
        )

    @keyword
    def validate_invalid_login_alert(self):
        try:
            WebDriverWait(
                self.selenium.driver,
                10
            ).until(
                EC.alert_is_present()
            )
            alert = Alert(self.selenium.driver)
            print(alert.text)
            alert.accept()
        except TimeoutException:
            raise AssertionError(
                "Invalid login alert not displayed"
            )