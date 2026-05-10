from behave import *
from pages.login_page import LoginPage
from pages.leave_page import LeavePage
import time


@given('employee logs into OrangeHRM')
def step_impl(context):

    login = LoginPage(context.driver)

    login.open_url()
    login.enter_username("Admin")
    login.enter_password("admin123")
    login.click_login()


@when('employee applies for medical leave')
def step_impl(context):

    context.leave = LeavePage(context.driver)

    time.sleep(3)

    context.leave.click_leave()

    time.sleep(2)

    context.leave.click_apply()

    time.sleep(2)


@then('leave apply page should display')
def step_impl(context):

    assert "leave" in context.driver.current_url.lower()