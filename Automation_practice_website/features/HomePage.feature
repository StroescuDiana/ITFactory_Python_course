@Test_Case_10
Feature: Subscription
  Scenario: Verify Subscription in home page
    When Launch browser
    When Navigate to url "http://automationexercise.com"
    When Verify that home page is visible successfully
    When Scroll down to footer
    When Verify text "SUBSCRIPTION"
    When Enter email address in input and click arrow button
    Then Verify success message "You have been successfully subscribed!" is visible