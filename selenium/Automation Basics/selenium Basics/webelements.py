import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver=webdriver.Edge()
driver.maximize_window()
driver.get("https://www.selenium.dev/selenium/web/web-form.html")
time.sleep(5)
#text input
text_input=driver.find_element(By.ID,"my-text-id")
text_input.clear()
text_input.send_keys("selenium WebDriver Demo")

#PASSWORD INPUT
password_input=driver.find_element(By.NAME,"my-password")
password_input.clear()
password_input.send_keys("secret123")

#TEXTAREA

textarea=driver
time.sleep(5)
driver.quit()