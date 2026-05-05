from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support
from selenium.common.exceptions import NoSuchElementException
import time

driver = webdriver.Edge(service=Service('../resources/msedgedriver.exe'))
# open Google
driver.get("https://www.google.com")
#implicity
# driver.implicity_Wait(5)
# search_box=driver.find_element(By.NAME,"q")
# search_box.send_keys("selenium")
# googlesearch_button=driver.find_element(By.NAME,"btnK")
# googlesearch_button.click()
#explicitly
# wait=WebDriverWait(driver,10)
# search_box=wait.until(EC.visibility_of_element_located((By.NAME,"q")))
# search_box.send_keys("Explict wait")
# googlesearch_button=wait.until(EC.element(By.NAME,"btnK"))
# googlesearch_button.click()



# explicit wait
wait = WebDriverWait(
    driver,
    timeout=10,
    poll_frequency=0.5,
    ignored_exceptions=[NoSuchElementException]
)
# locate search box and type
search_box = wait.until(selenium.webdriver.support.expected_condition.visibility_of_element_located((By.NAME, "q")))
search_box.send_keys("Explicit Wait")
# locate I'm Feeling Lucky button and click
imfl_button = wait.until(selenium.webdriver.support.expected_condition.element_to_be_clickable((By.NAME, "btnI")))
imfl_button.click()
time.sleep(3)
driver.quit()
