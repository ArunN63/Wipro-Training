# Import required libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# ==============================
# Common setup function
# ==============================
def setup_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get("https://www.amazon.in")
    return driver
# ==============================
# Handle popup (Continue Shopping etc.)
# ==============================
def handle_popup(driver):
    try:
        wait = WebDriverWait(driver, 5)
        # Example: Continue Shopping button
        popup = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Continue shopping')]"))
        )
        popup.click()
        print("Popup handled")
    except:
        print("No popup appeared")


# =========================================
# Exercise 1
# =========================================
def test_navigation_title():
    driver = setup_driver()
    wait = WebDriverWait(driver, 15)
    handle_popup(driver)
    wait.until(EC.presence_of_element_located((By.ID, "twotabsearchtextbox")))
    title = driver.title
    print("Title:", title)
    assert "Amazon" in title
    driver.find_element(By.LINK_TEXT, "Mobiles").click()
    wait.until(EC.title_contains("Mobile"))
    driver.back()
    driver.save_screenshot("ex1.png")  # proof
    time.sleep(5)
    driver.quit()


# =========================================
# Exercise 2
# =========================================
def test_search_headphones():
    driver = setup_driver()
    wait = WebDriverWait(driver, 15)
    handle_popup(driver)
    search_box = wait.until(EC.visibility_of_element_located((By.ID, "twotabsearchtextbox")))
    search_box.clear()  # IMPORTANT FIX
    search_box.send_keys("Wireless Headphones")
    search_button = driver.find_element(By.XPATH, "//input[@id='nav-search-submit-button']")
    search_button.click()
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.s-main-slot")))
    print("Search results loaded")
    driver.save_screenshot("ex2.png")
    assert "wireless headphones" in driver.page_source.lower()
    time.sleep(5)
    driver.quit()
# =========================================
# Exercise 3
# =========================================
def test_laptop_search_waits():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://www.amazon.in")
    handle_popup(driver)
    driver.find_element(By.ID, "twotabsearchtextbox").send_keys("Dell Laptop")
    driver.find_element(By.ID, "nav-search-submit-button").click()
    wait = WebDriverWait(driver, 15)
    results_grid = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.s-main-slot")))
    first_product = results_grid.find_element(By.CSS_SELECTOR, "div[data-component-type='s-search-result'] h2 a")
    first_product.click()
    driver.save_screenshot("ex3.png")
    time.sleep(5)
    driver.quit()
# =========================================
# Exercise 4
# =========================================
def test_footer_links():
    driver = setup_driver()
    wait = WebDriverWait(driver, 15)
    handle_popup(driver)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    about_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href*='aboutamazon']")))
    about_link.click()
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    element = driver.find_element(By.LINK_TEXT, "Careers")
    print("Text:", element.text)
    driver.save_screenshot("ex4.png")
    time.sleep(5)
    driver.quit()
# =========================================
# Exercise 5
# =========================================
def test_smartwatch_filter():
    driver = setup_driver()
    wait = WebDriverWait(driver, 15)
    handle_popup(driver)
    search_box = wait.until(EC.visibility_of_element_located((By.ID, "twotabsearchtextbox")))
    search_box.clear()
    search_box.send_keys("Smart Watches")
    driver.find_element(By.ID, "nav-search-submit-button").click()
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.s-main-slot")))
    brand_filter = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Apple']")))
    brand_filter.click()
    # Wait for page refresh
    wait.until(EC.staleness_of(driver.find_element(By.CSS_SELECTOR, "div.s-main-slot")))
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.s-main-slot")))
    products = driver.find_elements(By.CSS_SELECTOR, "div.s-search-result")
    print("Product count:", len(products))
    driver.save_screenshot("ex5.png")
    time.sleep(5)
    driver.quit()