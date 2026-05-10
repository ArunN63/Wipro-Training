from pages.home_page import HomePage


class TestExercise2:
    def test_phones_category_products(self, driver):
        """Test getting all product names from Phones category"""
        home = HomePage(driver)
        phones_page = home.click_phones()
        product_names = phones_page.get_all_product_names()

        assert "Samsung galaxy s6" in product_names, "Samsung galaxy s6 not found in phones list"
        print(f"✓ Exercise 2 passed: Found {len(product_names)} products including 'Samsung galaxy s6'")