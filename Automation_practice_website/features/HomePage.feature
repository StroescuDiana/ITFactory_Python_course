Feature: Subscription
  @Test_case_10
  Scenario: Verify Subscription on the home page
    Given I am on the Home page
    When I scroll down to the footer
    And I verify that the "SUBSCRIPTION" text is visible
    And I enter an email address in the input and click the arrow button
    Then I should see the success message "You have been successfully subscribed!"