import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get('https://the-internet.herokuapp.com/javascript_alerts')
    yield driver
    driver.quit()
# 1️⃣ Simple JS Alert
def test_js_alert(driver):
    wait = WebDriverWait(driver, 10)
    driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()
    alert = wait.until(EC.alert_is_present())
    assert alert.text == "I am a JS Alert"
    alert.accept()
    result = wait.until(EC.visibility_of_element_located((By.ID, "result"))).text
    assert "You successfully clicked an alert" in result
# 2️⃣ JS Confirm (OK)
def test_js_confirm_ok(driver):
    wait = WebDriverWait(driver, 10)
    driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()
    alert = wait.until(EC.alert_is_present())
    assert alert.text == "I am a JS Confirm"
    alert.accept()
    result = wait.until(EC.visibility_of_element_located((By.ID, "result"))).text
    assert "You clicked: Ok" in result
# 3️⃣ JS Confirm (Cancel)
def test_js_confirm_cancel(driver):
    wait = WebDriverWait(driver, 10)
    driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()
    alert = wait.until(EC.alert_is_present())
    alert.dismiss()
    result = wait.until(EC.visibility_of_element_located((By.ID, "result"))).text
    assert "You clicked: Cancel" in result
# 4️⃣ JS Prompt
def test_js_prompt(driver):
    wait = WebDriverWait(driver, 10)
    driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']").click()
    alert = wait.until(EC.alert_is_present())
    assert alert.text == "I am a JS prompt"
    alert.send_keys("Arun")
    alert.accept()
    result = wait.until(EC.visibility_of_element_located((By.ID, "result"))).text
    assert "You entered: Arun" in result