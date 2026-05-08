

Feature:Search
  Scenario: Search for a product with results
    Given Buyer is on the OLX homepage
    When buyer types product in search_input
    Then search result should be displayed

  Scenario: Search for a product with no results
    Given Buyer is on the OLX homepage
    When buyer types product in search_input
    Then Error message should be displayed



