from pytest_bdd import scenarios, given, when, then, parsers
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.myinfo_page import MyInfoPage

scenarios('../features/profile_update.feature')

@given('I am logged in as "Admin" with password "admin123"')
def login_as_admin(driver):
    login_page = LoginPage(driver)
    login_page.login("Admin", "admin123")

@given('I navigate to "My Info" section')
def navigate_to_myinfo(driver):
    dashboard = DashboardPage(driver)
    dashboard.navigate_to_myinfo()

@when('I click on "Personal Details"')
def click_personal_details(driver):
    myinfo_page = MyInfoPage(driver)
    myinfo_page.click_personal_details()

@when(parsers.parse('I change my nickname to "{nickname}"'))
def change_nickname(driver, nickname):
    myinfo_page = MyInfoPage(driver)
    myinfo_page.update_nickname(nickname)

@when(parsers.parse('I upload a profile photograph "{photo_file}"'))
def upload_photo(driver, photo_file):
    myinfo_page = MyInfoPage(driver)
    myinfo_page.upload_profile_photo(photo_file)

@when('I click on "Save" button')
def click_save(driver):
    myinfo_page = MyInfoPage(driver)
    myinfo_page.click_save()

@then('I should see a success message "Successfully Updated"')
def verify_success_message(driver):
    myinfo_page = MyInfoPage(driver)
    message = myinfo_page.get_success_message()
    assert "Success" in message or "Updated" in message, f"Expected success message, got {message}"

@then(parsers.parse('my nickname should be displayed as "{nickname}"'))
def verify_nickname(driver, nickname):
    myinfo_page = MyInfoPage(driver)
    current_nickname = myinfo_page.get_nickname()
    assert current_nickname == nickname, f"Expected nickname '{nickname}', got '{current_nickname}'"

@then('my profile picture should be visible')
def verify_profile_picture(driver):
    myinfo_page = MyInfoPage(driver)
    assert myinfo_page.is_profile_picture_visible(), "Profile picture is not visible"

# Contact details scenario
@when('I click on "Contact Details"')
def click_contact_details(driver):
    myinfo_page = MyInfoPage(driver)
    myinfo_page.click_contact_details()

@when(parsers.parse('I update my mobile number to "{mobile_number}"'))
def update_mobile(driver, mobile_number):
    myinfo_page = MyInfoPage(driver)
    myinfo_page.update_mobile_number(mobile_number)

@when('I save the changes')
def save_changes(driver):
    myinfo_page = MyInfoPage(driver)
    myinfo_page.click_save()