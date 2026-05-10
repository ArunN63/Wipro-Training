from behave import *
from pages.login_page import LoginPage


@given('user launches OrangeHRM login page')
def step_impl(context):

    context.login = LoginPage(context.driver)
    context.login.open_url()


@when('user enters username "{username}"')
def step_impl(context, username):

    context.login.enter_username(username)


@when('user enters password "{password}"')
def step_impl(context, password):

    context.login.enter_password(password)


@when('user clicks login button')
def step_impl(context):

    context.login.click_login()


@then('user should navigate to dashboard')
def step_impl(context):

    assert "dashboard" in context.driver.current_url.lower()


@then('invalid credentials message should display')
def step_impl(context):

    error = context.login.get_invalid_message()

    assert error == "Invalid credentials"