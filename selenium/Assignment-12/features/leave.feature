Feature: Leave Application

  Scenario: Apply medical leave

    Given employee logs into OrangeHRM
    When employee applies for medical leave
    Then leave apply page should display