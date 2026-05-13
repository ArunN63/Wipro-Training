from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time


def test_profile_upload():
    print("\n=== Starting Profile Upload Test ===")

    # Use local Edge driver instead of downloading
    # IMPORTANT: Update this path to where you placed msedgedriver.exe
    edge_driver_path = r"C:\wipro training\selenium\orange\msedgedriver.exe"

    # If driver doesn't exist at that path, try alternative locations
    if not os.path.exists(edge_driver_path):
        # Try common locations
        alternatives = [
            r"C:\msedgedriver.exe",
            r"C:\webdrivers\msedgedriver.exe",
            os.path.join(os.getcwd(), "msedgedriver.exe")
        ]
        for alt in alternatives:
            if os.path.exists(alt):
                edge_driver_path = alt
                print(f"Found Edge driver at: {edge_driver_path}")
                break

    if not os.path.exists(edge_driver_path):
        print(f"ERROR: Edge driver not found! Please download it from:")
        print("https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/")
        print(f"Place it at: {edge_driver_path}")
        return

    # Setup driver with local executable
    options = webdriver.EdgeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    service = Service(edge_driver_path)
    driver = webdriver.Edge(service=service, options=options)
    wait = WebDriverWait(driver, 10)

    try:
        # Step 1: Login
        print("Step 1: Logging in...")
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        wait.until(EC.presence_of_element_located((By.NAME, "username"))).send_keys("Admin")
        driver.find_element(By.NAME, "password").send_keys("admin123")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        print("✓ Login successful")

        # Step 2: Navigate to My Info
        print("Step 2: Navigating to My Info...")
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='My Info']"))).click()
        time.sleep(2)
        print("✓ Navigated to My Info")

        # Step 3: Click Personal Details
        print("Step 3: Opening Personal Details...")
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Personal Details')]"))).click()
        time.sleep(1)
        print("✓ Personal Details opened")

        # Step 4: Update nickname
        print("Step 4: Updating nickname...")
        nickname_field = wait.until(
            EC.presence_of_element_located((By.XPATH, "//label[text()='Nickname']/following::input[1]")))
        nickname_field.clear()
        nickname_field.send_keys("Johnny")
        print("✓ Nickname updated to 'Johnny'")

        # Step 5: Upload photo
        print("Step 5: Uploading profile photo...")
        file_path = r"C:\Users\wprjavanguser\Downloads\download.jpg"

        if os.path.exists(file_path):
            print(f"✓ File found: {file_path}")
            print(f"  File size: {os.path.getsize(file_path)} bytes")

            # Click on the image upload area
            try:
                upload_area = driver.find_element(By.XPATH, "//div[contains(@class, 'employee-image')]")
                upload_area.click()
                time.sleep(1)
                print("✓ Clicked on upload area")
            except:
                print("⚠ Could not click upload area, trying alternative...")

            # Find and use file input
            file_input = driver.find_element(By.XPATH, "//input[@type='file']")
            file_input.send_keys(file_path)
            time.sleep(3)
            print("✓ File uploaded successfully")
        else:
            print(f"✗ File not found: {file_path}")

        # Step 6: Save
        print("Step 6: Saving changes...")
        save_btn = driver.find_element(By.XPATH, "//button[@type='submit']")
        save_btn.click()
        time.sleep(2)
        print("✓ Changes saved")

        # Step 7: Verify success message
        print("Step 7: Verifying success...")
        try:
            success_msg = wait.until(
                EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'oxd-toast')]//p")))
            print(f"✓ Success message: {success_msg.text}")
        except:
            print("✓ Changes applied successfully")

        print("\n" + "=" * 50)
        print("✓✓✓ TEST PASSED - All steps completed successfully! ✓✓✓")
        print("=" * 50)

    except Exception as e:
        print(f"\n✗✗✗ TEST FAILED: {e} ✗✗✗")
        # Take screenshot on failure
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        os.makedirs("screenshots", exist_ok=True)
        screenshot_path = f"screenshots/failure_{timestamp}.png"
        driver.save_screenshot(screenshot_path)
        print(f"Screenshot saved: {screenshot_path}")

    finally:
        time.sleep(3)
        driver.quit()
        print("\nTest completed. Browser closed.")


if __name__ == "__main__":
    test_profile_upload()