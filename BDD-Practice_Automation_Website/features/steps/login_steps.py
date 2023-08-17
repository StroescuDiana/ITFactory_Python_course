from behave import given, when, then

from pages.login_page import LoginPage


@given('I am on the login page')
def step_impl(context):
    context.page = LoginPage()
    context.page.load()


@when('I enter my username and password')
def step_impl(context):
    context.page.set_username(context.config.userdata['username'])
    context.page.set_password(context.config.userdata['password'])


@when('I click the login button')
def step_impl(context):
    context.page.click_login()


@then('I should be redirected to the home page')
def step_impl(context):
    assert str(context.page.get_title()).lower() == "logged in successfully | practice test automation", "Page title is not as expected"
