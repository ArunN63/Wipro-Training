from pages.home_page import HomePage

class TestExercise1:
    def test_laptops_category_navigation(self, driver):
        """Test navigation to Laptops category"""
        home = HomePage(driver)
        home.click_laptops().verify_laptop_list_presence()
        print("✓ Exercise 1 passed: Laptops category navigation successful")