from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time
import os


class MyInfoPage(BasePage):
    # Locators - Personal Details
    PERSONAL_DETAILS_TAB = (By.XPATH, "//a[contains(text(), 'Personal Details')]")
    CONTACT_DETAILS_TAB = (By.XPATH, "//a[contains(text(), 'Contact Details')]")
    EMERGENCY_CONTACTS_TAB = (By.XPATH, "//a[contains(text(), 'Emergency Contacts')]")
    DEPENDENTS_TAB = (By.XPATH, "//a[contains(text(), 'Dependents')]")
    IMMIGRATION_TAB = (By.XPATH, "//a[contains(text(), 'Immigration')]")
    JOB_TAB = (By.XPATH, "//a[contains(text(), 'Job')]")

    # Personal Details Fields
    FIRST_NAME_INPUT = (By.NAME, "firstName")
    LAST_NAME_INPUT = (By.NAME, "lastName")
    NICKNAME_INPUT = (By.XPATH, "//label[text()='Nickname']/following::input[1]")
    EMPLOYEE_ID_INPUT = (By.XPATH, "//label[text()='Employee Id']/following::input[1]")
    DRIVERS_LICENSE_INPUT = (By.XPATH, "//label[text()='Driver's License Number']/following::input[1]")
    LICENSE_EXPIRY_DATE = (By.XPATH, "//label[text()='License Expiry Date']/following::input[1]")
    SSN_NUMBER_INPUT = (By.XPATH, "//label[text()='SSN Number']/following::input[1]")
    SIN_NUMBER_INPUT = (By.XPATH, "//label[text()='SIN Number']/following::input[1]")
    NATIONALITY_DROPDOWN = (By.XPATH, "(//div[contains(@class, 'oxd-select-text')])[1]")
    MARITAL_STATUS_DROPDOWN = (By.XPATH, "(//div[contains(@class, 'oxd-select-text')])[2]")
    DATE_OF_BIRTH_INPUT = (By.XPATH, "//label[text()='Date of Birth']/following::input[1]")
    GENDER_MALE_RADIO = (By.XPATH, "//label[text()='Male']/span")
    GENDER_FEMALE_RADIO = (By.XPATH, "//label[text()='Female']/span")

    # Profile Picture
    PROFILE_PICTURE = (By.XPATH, "//img[contains(@class, 'employee-image')]")
    UPLOAD_BUTTON = (By.XPATH, "//button[contains(@class, 'image-upload')]")
    FILE_INPUT = (By.XPATH, "//input[@type='file']")
    DELETE_PHOTO_BUTTON = (By.XPATH, "//button[contains(@class, 'image-delete')]")

    # Contact Details Fields
    MOBILE_NUMBER_INPUT = (By.XPATH, "//label[text()='Mobile']/following::input[1]")
    HOME_NUMBER_INPUT = (By.XPATH, "//label[text()='Home']/following::input[1]")
    WORK_NUMBER_INPUT = (By.XPATH, "//label[text()='Work']/following::input[1]")
    WORK_EMAIL_INPUT = (By.XPATH, "//label[text()='Work Email']/following::input[1]")
    OTHER_EMAIL_INPUT = (By.XPATH, "//label[text()='Other Email']/following::input[1]")
    ADDRESS_STREET_INPUT = (By.XPATH, "//label[text()='Street 1']/following::input[1]")
    ADDRESS_CITY_INPUT = (By.XPATH, "//label[text()='City']/following::input[1]")
    ADDRESS_STATE_INPUT = (By.XPATH, "//label[text()='State/Province']/following::input[1]")
    ADDRESS_ZIP_INPUT = (By.XPATH, "//label[text()='Zip/Postal Code']/following::input[1]")
    ADDRESS_COUNTRY_DROPDOWN = (By.XPATH,
                                "//label[text()='Country']/following::div[contains(@class, 'oxd-select-text')]")

    # Action Buttons
    SAVE_BUTTON = (By.XPATH, "//button[@type='submit']")
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(@class, 'oxd-toast')]//p[contains(text(), 'Success')]")

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

    def get_nickname(self):
        """Get current nickname value"""
        nickname_field = self.find(self.NICKNAME_INPUT)
        return nickname_field.get_attribute('value')

    def upload_profile_photo(self, photo_filename):
        """Upload profile photograph"""
        # Create uploads directory if it doesn't exist
        uploads_dir = "uploads"
        if not os.path.exists(uploads_dir):
            os.makedirs(uploads_dir)

        # Create a dummy image if it doesn't exist
        photo_path = os.path.join(uploads_dir, photo_filename)
        if not os.path.exists(photo_path):
            # Create a simple text file as placeholder (or you can add an actual image)
            with open(photo_path, 'w') as f:
                f.write("This is a placeholder for profile image")

        # Click upload button to trigger file dialog
        self.click(self.UPLOAD_BUTTON)
        time.sleep(1)

        # Send file path to file input
        file_input = self.find(self.FILE_INPUT)
        file_input.send_keys(os.path.abspath(photo_path))
        time.sleep(2)

        self.logger.info(f"Uploaded profile photo: {photo_filename}")
        return self

    def is_profile_picture_visible(self):
        """Check if profile picture is displayed"""
        try:
            return self.find(self.PROFILE_PICTURE).is_displayed()
        except:
            return False

    def update_mobile_number(self, mobile_number):
        """Update mobile number"""
        self.click_contact_details()
        mobile_field = self.find(self.MOBILE_NUMBER_INPUT)
        mobile_field.clear()
        mobile_field.send_keys(mobile_number)
        return self

    def click_save(self):
        """Click Save button"""
        save_button = self.wait_for_element_clickable(self.SAVE_BUTTON)
        save_button.click()
        time.sleep(2)
        return self

    def get_success_message(self):
        """Get success message text"""
        message = self.find(self.SUCCESS_MESSAGE)
        return message.text