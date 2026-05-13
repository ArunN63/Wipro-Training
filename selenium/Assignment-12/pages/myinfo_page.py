from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time
import os


class MyInfoPage(BasePage):
    # Locators
    PERSONAL_DETAILS_TAB = (By.XPATH, "//a[contains(text(), 'Personal Details')]")
    CONTACT_DETAILS_TAB = (By.XPATH, "//a[contains(text(), 'Contact Details')]")
    NICKNAME_INPUT = (By.XPATH, "//label[text()='Nickname']/following::input[1]")
    PROFILE_PICTURE = (By.XPATH, "//img[contains(@class, 'employee-image')]")
    UPLOAD_BUTTON = (By.XPATH, "//button[contains(@class, 'image-upload')]")
    FILE_INPUT = (By.XPATH, "//input[@type='file']")
    SAVE_BUTTON = (By.XPATH, "//button[@type='submit']")
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(@class, 'oxd-toast')]//p[contains(text(), 'Success')]")
    MOBILE_NUMBER_INPUT = (By.XPATH, "//label[text()='Mobile']/following::input[1]")
    DISPLAYED_NICKNAME = (By.XPATH, "//label[text()='Nickname']/following::input[1]")
    PROFILE_IMAGE = (By.XPATH, "//img[contains(@class, 'employee-image')]")

    def click_personal_details(self):
        """Click on Personal Details tab"""
        self.click(self.PERSONAL_DETAILS_TAB)
        time.sleep(1)
        return self

    def click_contact_details(self):
        """Click on Contact Details tab"""
        self.click(self.CONTACT_DETAILS_TAB)
        time.sleep(1)
        return self

    def update_nickname(self, nickname):
        """Update nickname field"""
        nickname_field = self.find(self.NICKNAME_INPUT)
        nickname_field.clear()
        nickname_field.send_keys(nickname)
        self.logger.info(f"Updated nickname to: {nickname}")
        return self

    def upload_profile_photo(self, photo_filename):
        """Upload profile photograph"""
        # Create uploads directory if it doesn't exist
        uploads_dir = "uploads"
        if not os.path.exists(uploads_dir):
            os.makedirs(uploads_dir)

        # Full path to the photo
        photo_path = os.path.join(uploads_dir, photo_filename)

        # Click upload button to trigger file dialog
        self.click(self.UPLOAD_BUTTON)
        time.sleep(1)

        # Send file path to file input
        file_input = self.find(self.FILE_INPUT)
        file_input.send_keys(os.path.abspath(photo_path))
        time.sleep(2)

        self.logger.info(f"Uploaded profile photo: {photo_filename}")
        return self

    def click_save(self):
        """Click Save button"""
        self.click(self.SAVE_BUTTON)
        time.sleep(2)
        return self

    def get_success_message(self):
        """Get success message text"""
        message = self.find(self.SUCCESS_MESSAGE)
        return message.text

    def get_nickname(self):
        """Get current nickname value"""
        nickname_field = self.find(self.DISPLAYED_NICKNAME)
        return nickname_field.get_attribute('value')

    def is_profile_picture_visible(self):
        """Check if profile picture is displayed"""
        try:
            return self.find(self.PROFILE_IMAGE).is_displayed()
        except:
            return False

    def update_mobile_number(self, mobile_number):
        """Update mobile number"""
        mobile_field = self.find(self.MOBILE_NUMBER_INPUT)
        mobile_field.clear()
        mobile_field.send_keys(mobile_number)
        return self