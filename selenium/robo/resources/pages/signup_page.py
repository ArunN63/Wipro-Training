# import sys
# import os
# from typing import cast
#
#
# sys.path.append(
#     os.path.abspath(
#         os.path.join(os.path.dirname(__file__), "../..")
#     )
# )
#
# from SeleniumLibrary import SeleniumLibrary
#
# from robot.api.deco import keyword
# from selenium.webdriver.common.alert import Alert
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException
#
# from robot.libraries.BuiltIn import BuiltIn
#
# from libraries.logger import LogGen
# from resources.locators.signup_locators import (
#     SIGNUP_LINK,
#     USERNAME_TEXTBOX,
#     PASSWORD_TEXTBOX,
#     SIGNUP_BUTTON
# )
#
# from resources.variables.config import config
#
# from resources.variables.testdata import (
#     SIGNUP_USERNAME,
#     SIGNUP_PASSWORD
# )
# class SignupPage:
#
#     @property
#     def selenium(self):
#         return cast(
#             SeleniumLibrary,
#             BuiltIn().get_library_instance(
#                 "SeleniumLibrary"
#             )
#         )
#
#     @keyword
#     def launch_demoblaze_application(self):
#         self.selenium.open_browser(
#             url=config.base_url,
#             browser=config.browser
#         )
#         self.selenium.maximize_browser_window()
#         self.selenium.set_selenium_implicit_wait(
#             config.implicit_wait
#         )
#
#     @keyword
#     def click_signup_link(self):
#         self.selenium.click_element(
#             SIGNUP_LINK
#         )
#
#     @keyword
#     def enter_username(self):
#         self.selenium.input_text(
#             USERNAME_TEXTBOX,
#             SIGNUP_USERNAME
#         )
#
#     @keyword
#     def enter_password(self):
#         self.selenium.input_text(
#             PASSWORD_TEXTBOX,
#             SIGNUP_PASSWORD
#         )
#
#     @keyword
#     def click_register_button(self):
#         self.selenium.click_button(
#             SIGNUP_BUTTON
#         )
#
#     @keyword
#     def verify_signup_success_alert(self):
#         try:
#             WebDriverWait(
#                 self.selenium.driver,
#                 10
#             ).until(
#                 EC.alert_is_present()
#             )
#
#             alert = Alert(self.selenium.driver)
#
#             print(alert.text)
#
#             alert.accept()
#
#         except TimeoutException:
#             raise AssertionError(
#                 "Signup alert did not appear"
#             )