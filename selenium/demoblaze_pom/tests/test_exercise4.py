from pages.home_page import HomePage
import allure


class TestExercise4:
    @allure.title("Test complete checkout flow")
    def test_checkout_process(self, driver):
        """Test multi-step checkout process"""
        # Step 1: Add product to cart
        with allure.step("Navigate to Laptops and add Sony vaio i5 to cart"):
            home = HomePage(driver)
            laptops_page = home.click_laptops()
            product_page = laptops_page.click_product("Sony vaio i5")
            product_page.add_product_to_cart()

        # Step 2: Go to cart
        with allure.step("Navigate to Cart"):
            driver.get("https://www.demoblaze.com/cart.html")
            from pages.cart_page import CartPage
            cart_page = CartPage(driver)

        # Step 3: Place order and fill form
        with allure.step("Place order and fill purchase form"):
            purchase_modal = cart_page.click_place_order()

            purchase_data = {
                'name': 'John Doe',
                'country': 'United States',
                'city': 'New York',
                'card': '1234567890123456',
                'month': '12',
                'year': '2025'
            }

            purchase_modal.fill_purchase_form(purchase_data)
            purchase_modal.click_purchase()

        # Step 4: Verify success message
        with allure.step("Verify success message"):
            success_message = purchase_modal.get_success_message()
            assert "Thank you for your purchase" in success_message
            print(f"✓ Exercise 4 passed: {success_message}")