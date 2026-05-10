Feature: Admin User Search

  Scenario: Search users using data table

    Given admin is logged into system

    When admin searches user with following details
      | Username | Admin |
      | Role     | Admin |
      | Status   | Enabled |

    Then matching records should display