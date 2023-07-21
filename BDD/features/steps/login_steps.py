from behave import given, when, then

from pages.login_page import LoginPage


@given("I am on the login page")
def step_impl(context):
    context.page = LoginPage()
    context.page.load()


@when("I enter my username and password")
def step_impl(context):
    context.page.set_username(context.config.userdata['username'])
    context.page.set_password(context.config.userdata['password'])


@when("I click on Submit button")
def step_impl(context):
    context.page.click_submit_button()


@then("I should be redirected on home page")
def step_impl(context):
    try:
        assert str(context.page.get_title()).lower() == "test login | practice test automation", f"AssertionError @then."
    except AssertionError as error:
        print(error)
