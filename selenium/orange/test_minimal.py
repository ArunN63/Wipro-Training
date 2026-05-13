from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time


def test_minimal():
    print("\n=== Minimal Test ===")

    options = webdriver.EdgeOptions()
    options.add_argument("--start-maximized")

    service = Service(EdgeChromiumDriverManager().install())
    driver = webdriver.Edge(service=service, options=options)

    try:
        # Just test login
        driver.get("https://opensource-demo.orangehrmlive.com/")
        wait = WebDriverWait(driver, 10)

        username = wait.until(EC.presence_of_element_located((By.NAME, "username")))
        username.send_keys("Admin")
        driver.find_element(By.NAME, "password").send_keys("admin123")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()

        # Verify dashboard
        wait.until(EC.presence_of_element_located((By.XPATH, "//h6[text()='Dashboard']")))
        print("✓ Login successful!")

        print("✓ Test passed!")

    except Exception as e:
        print(f"✗ Test failed: {e}")

    finally:
        time.sleep(2)
        driver.quit()


if __name__ == "__main__":
    test_minimal()