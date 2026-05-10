from pages.home_page import HomePage


class TestExercise3:
    def test_add_to_cart_with_alert(self, driver):
        """Test adding product to cart and handling alert"""
        home = HomePage(driver)

        laptops_page = home.click_laptops()
        product_page = laptops_page.click_product("Sony vaio i5")
        product_page.add_product_to_cart()

        print("✓ Exercise 3 passed: Product added to cart and alert handled")