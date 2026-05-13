# Test data for various scenarios

EMPLOYEE_TEST_DATA = [
    {"first_name": "John", "last_name": "Wick"},
    {"first_name": "Sarah", "last_name": "Johnson"},
    {"first_name": "Michael", "last_name": "Chen"},
    {"first_name": "Emma", "last_name": "Rodriguez"},
    {"first_name": "William", "last_name": "Turner"}
]

SEARCH_CRITERIA = {
    "admin_enabled": {"username": "Admin", "user_role": "Admin", "status": "Enabled"},
    "disabled_ess": {"user_role": "ESS", "status": "Disabled"}
}

PURCHASE_DATA = {
    "name": "Test User",
    "country": "Test Country",
    "city": "Test City",
    "card": "1234567890123456",
    "month": "12",
    "year": "2025"
}