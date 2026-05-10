Feature: Employee Management

  Scenario Outline: Add multiple employees

    Given admin logs into OrangeHRM
    When admin navigates to PIM module
    And admin adds employee with firstname "<firstname>" and lastname "<lastname>"
    Then employee should be added successfully

    Examples:
      | firstname | lastname |
      | John      | David    |
      | Steve     | Smith    |
      | Robert    | James    |