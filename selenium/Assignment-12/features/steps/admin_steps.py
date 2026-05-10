from behave import *
from pages.login_page import LoginPage
from pages.admin_page import AdminPage
import time


@given('admin is logged into system')
def step_impl(context):

    login = LoginPage(context.driver)

    login.open_url()
    login.enter_username("Admin")
    login.enter_password("admin123")
    login.click_login()


@when('admin searches user with following details')
def step_impl(context):

    context.admin = AdminPage(context.driver)

    time.sleep(3)

    context.admin.click_admin()

    data = {row[0]: row[1] for row in context.table}

    context.admin.enter_username(data["Username"])

    context.admin.click_search()

    time.sleep(3)


@then('matching records should display')
def step_impl(context):

    records = context.admin.get_records()

    assert len(records) > 0