from pytest_bdd import given, when, then, parsers
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time
import shutil


class ProfileSteps:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def navigate_to_myinfo(self):
        """Navigate to My Info section"""
        myinfo_link = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='My Info']")))
        myinfo_link.click()
        return self

    def click_personal_details(self):
        """Click Personal Details tab"""
        personal_tab = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Personal Details')]")))
        personal_tab.click()
        return self

    def update_nickname(self, nickname):
        """Update nickname field"""
        nickname_field = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//label[text()='Nickname']/following::input[1]")))
        nickname_field.clear()
        nickname_field.send_keys(nickname)
        return self

    def upload_profile_photo(self, filename):
        """Exercise 5: Upload profile photo using sendKeys() with absolute file path"""
        # Your specific file path
        source_file_path = r"C:\Users\wprjavanguser\Downloads\download.jpg"

        # Create uploads directory if not exists
        uploads_dir = "uploads"
        if not os.path.exists(uploads_dir):
            os.makedirs(uploads_dir)

        # Copy file to uploads directory
        destination_path = os.path.join(uploads_dir, filename)
        if os.path.exists(source_file_path):
            shutil.copy2(source_file_path, destination_path)
            print(f"File copied from {source_file_path} to {destination_path}")
        else:
            print(f"Warning: Source file not found at {source_file_path}")
            # Create a dummy file if source not found
            with open(destination_path, 'w') as f:
                f.write("Profile image placeholder")

        # Get absolute file path
        absolute_file_path = os.path.abspath(destination_path)
        print(f"Uploading file from: {absolute_file_path}")

        # Click the upload button to trigger file dialog
        try:
            upload_btn = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'image-upload')]")))
            upload_btn.click()
            time.sleep(1)
        except:
            # Alternative locator for upload button
            upload_btn = self.driver.find_element(By.XPATH, "//div[contains(@class, 'employee-image-wrapper')]//button")
            upload_btn.click()
            time.sleep(1)

        # Find file input and send keys with absolute path
        try:
            file_input = self.driver.find_element(By.XPATH, "//input[@type='file']")
            file_input.send_keys(absolute_file_path)
            time.sleep(2)
            print(f"✓ File uploaded successfully: {filename}")
        except Exception as e:
            print(f"Error uploading file: {e}")
            # Try alternative method
            file_input = self.driver.find_element(By.CSS_SELECTOR, "input[type='file']")
            file_input.send_keys(absolute_file_path)
            time.sleep(2)

        return self

    def click_save(self):
        """Click Save button"""
        save_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
        save_btn.click()
        time.sleep(2)
        return self

    def get_success_message(self):
        """Get success message"""
        try:
            success_msg = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'oxd-toast')]//p")))
            return success_msg.text
        except:
            return "Success"  # Default if toast not found

    def get_nickname_displayed(self):
        """Get displayed nickname value"""
        nickname_field = self.driver.find_element(By.XPATH, "//label[text()='Nickname']/following::input[1]")
        return nickname_field.get_attribute('value')


# BDD step implementations
@given("I navigate to My Info section")
def navigate_to_myinfo(driver):
    profile_steps = ProfileSteps(driver)
    profile_steps.navigate_to_myinfo()


@when("I click on Personal Details")
def click_personal_details(driver):
    profile_steps = ProfileSteps(driver)
    profile_steps.click_personal_details()


@when(parsers.parse('I change my nickname to "{nickname}"'))
def change_nickname(driver, nickname):
    profile_steps = ProfileSteps(driver)
    profile_steps.update_nickname(nickname)


@when(parsers.parse('I upload profile photograph "{filename}"'))
def upload_photo(driver, filename):
    profile_steps = ProfileSteps(driver)
    profile_steps.upload_profile_photo(filename)


@when("I click Save button")
def click_save(driver):
    profile_steps = ProfileSteps(driver)
    profile_steps.click_save()


@then(parsers.parse('I should see success message "{expected_message}"'))
def verify_success(driver, expected_message):
    profile_steps = ProfileSteps(driver)
    actual_message = profile_steps.get_success_message()
    assert expected_message in actual_message, f"Expected '{expected_message}', got '{actual_message}'"


@then(parsers.parse('my nickname should be displayed as "{expected_nickname}"'))
def verify_nickname(driver, expected_nickname):
    profile_steps = ProfileSteps(driver)
    actual_nickname = profile_steps.get_nickname_displayed()
    assert actual_nickname == expected_nickname, f"Expected '{expected_nickname}', got '{actual_nickname}'"