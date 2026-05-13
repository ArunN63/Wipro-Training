Feature: Admin User Search

  Background: Admin is logged in
    Given I open OrangeHRM login page
    And I enter username "Admin" and password "admin123"
    And I click login button
    And I navigate to Admin module

  Scenario: Search users with multiple filters
    When I enter the following search criteria:
      | Username  | User Role | Status  |
      | Admin     | Admin     | Enabled |
    Then I should see at least 1 result