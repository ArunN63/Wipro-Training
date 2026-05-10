import allure
from behave import given, when, then

from pages.signup_page import SignupPage
from utils.logger import LogGen
from utils.screenshot_util import ScreenshotUtil
from webdriver_manager.core.driver import Driver

logger = LogGen.loggen()


@given(u'User launches Demoblaze application')
def step_impl(context):
    logger.info('Demoblaze URL loaded')


@when(u'User clicks on Sign up menu')
def step_impl(context):
    logger.info("Step : Click signup Menu")
    context.signup_page = SignupPage(context.driver)
    context.signup_page.click_signup_menu()



@when(u'User enters signup username "{username}"')
def step_impl(context, username):
    logger.info(f"Step : Enter Username : {username}")
    context.signup_page.enter_username(username)


@when(u'User enters signup password "{password}"')
def step_impl(context, password):
    logger.info(f"Step : Enter Password : {password}")
    context.signup_page.enter_password(password)


@when(u'User clicks Signup button')
def step_impl(context):
    logger.info(f"Step : Click Sign Up button ")
    context.signup_page.click_signup_button()



@then(u'User should see signup success message')
def step_impl(context):
    logger.info("Step : Verify Successful Sign up Message")
    context.signup_page.verify_successful_sign_up()
    screenshot_path = (ScreenshotUtil.capture_screenshot(context.driver, "successful_signup"))
    logger.info(f"Screenshot Captured : {screenshot_path}")
    allure.attach(context.driver.get_screenshot_as_png(), name="Successful SignUp",
                  attachment_type=allure.attachment_type.PNG)

