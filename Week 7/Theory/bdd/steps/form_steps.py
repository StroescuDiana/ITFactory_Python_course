from behave import *
from selenium import webdriver

@given('I am on the login page')
def go_to_form(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://formy-project.herokuapp.com/form")

@when('I enter my username and password')
def fill_form(context):
    # Fill first name, last name, job title, education, sex, experience and date
        pass

@when('I click submit')
def click_submit(context):
    # Click submit button
    pass

@then('I should see a success message')
def see_success(context):
    # Verify success message is displayed
    pass