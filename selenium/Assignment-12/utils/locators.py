from selenium.webdriver.common.by import By


class LoginLocators:

    USERNAME = (By.NAME, "username")
    PASSWORD = (By.NAME, "password")
    LOGIN_BUTTON = (
        By.XPATH,
        "//button[@type='submit']"
    )

    ERROR_MESSAGE = (
        By.XPATH,
        "//p[contains(@class,'alert-content-text')]"
    )


class PimLocators:

    PIM_MENU = (
        By.XPATH,
        "//span[text()='PIM']"
    )

    ADD_EMPLOYEE = (
        By.XPATH,
        "//a[text()='Add Employee']"
    )

    FIRSTNAME = (
        By.NAME,
        "firstName"
    )

    LASTNAME = (
        By.NAME,
        "lastName"
    )

    SAVE_BUTTON = (
        By.XPATH,
        "//button[@type='submit']"
    )


class AdminLocators:

    ADMIN_MENU = (
        By.XPATH,
        "//span[text()='Admin']"
    )


class LeaveLocators:

    LEAVE_MENU = (
        By.XPATH,
        "//span[text()='Leave']"
    )


class ProfileLocators:

    MYINFO_MENU = (
        By.XPATH,
        "//span[text()='My Info']"
    )

    NICKNAME = (
        By.XPATH,
        "//input[@name='nickname']"
    )

    SAVE_BUTTON = (
        By.XPATH,
        "//button[@type='submit']"
    )