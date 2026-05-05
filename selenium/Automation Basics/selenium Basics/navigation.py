# setup Edge driver
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

driver = webdriver.Edge(service=Service('../resources/msedgedriver.exe'))
# open Google
driver.get("https://www.google.com")
time.sleep(3)
# open Wikipedia
driver.get("https://www.wikipedia.org/")
time.sleep(3)
# go back to Google
driver.back()
time.sleep(3)
# go forward to Wikipedia
driver.forward()
time.sleep(3)
# go back again
driver.back()
time.sleep(3)
# refresh the page
driver.refresh()
time.sleep(3)
# close browser
driver.quit()