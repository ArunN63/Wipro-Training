Feature: Admin User Search
  As a system administrator
  I want to search for users using multiple criteria
  So that I can filter the user list efficiently

  Background: Admin is logged into the system
    Given I am logged in as "Admin" with password "admin123"
    And I navigate to the Admin module

  @Regression @Admin
  Scenario: Search users with multiple filters using data table
    When I search for users with the following criteria:
      | Username  | User Role    | Status   |
      | Admin     | Admin        | Enabled  |
    Then I should see at least one user in the results
    And the search results should match the criteria

  Scenario: Search for disabled users
    When I search for users with the following criteria:
      | Username  | User Role     | Status    |
      |           | ESS           | Disabled  |
    Then the results should show only disabled ESS users