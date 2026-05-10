from behave import *
from pages.login_page import LoginPage
from pages.pim_page import PimPage
import time


@given('admin logs into OrangeHRM')
def step_impl(context):

    login = LoginPage(context.driver)

    login.open_url()
    login.enter_username("Admin")
    login.enter_password("admin123")
    login.click_login()


@when('admin navigates to PIM module')
def step_impl(context):

    context.pim = PimPage(context.driver)

    time.sleep(2)

    context.pim.click_pim()


@when('admin adds employee with firstname "{firstname}" and lastname "{lastname}"')
def step_impl(context, firstname, lastname):

    context.pim.click_add_employee()

    time.sleep(2)

    context.pim.enter_firstname(firstname)
    context.pim.enter_lastname(lastname)

    context.pim.click_save()

    time.sleep(3)


@then('employee should be added successfully')
def step_impl(context):

    assert "pim" in context.driver.current_url.lower()