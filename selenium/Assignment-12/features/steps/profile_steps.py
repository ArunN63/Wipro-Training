from behave import *
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
import os
import time


@given('user logs into OrangeHRM')
def step_impl(context):

    login = LoginPage(context.driver)

    login.open_url()
    login.enter_username("Admin")
    login.enter_password("admin123")
    login.click_login()


@when('user navigates to My Info page')
def step_impl(context):

    context.profile = ProfilePage(context.driver)

    time.sleep(3)

    context.profile.click_myinfo()


@when('user updates nickname as "{nickname}"')
def step_impl(context, nickname):

    time.sleep(2)

    context.profile.update_nickname(nickname)


@when('user uploads profile image')
def step_impl(context):

    image_path = os.path.abspath(
        "uploads/profile.jpg"
    )

    context.profile.upload_photo(image_path)

    time.sleep(2)


@then('profile should update successfully')
def step_impl(context):

    context.profile.click_save()

    time.sleep(2)

    assert "personalDetails" in context.driver.current_url