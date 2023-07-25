from behave import when, then

from pages.HomePage_base import HomePage


@when('Launch browser')
def step_impl(context):
    assert context.webdriver != None, f"webdriver is None"


@when('Navigate to url "http://automationexercise.com"')
def step_impl(context):
    context.page = HomePage()
    context.page.load_homepage()


@when('Verify that home page is visible successfully')
def step_impl(context):
    context.page.home_page_is_visible()


@when('Scroll down to footer')
def step_impl(context):
    context.page.scroll_to_footer()


@when('Verify text "SUBSCRIPTION"')
def step_impl(context):
    context.page.verify_text()


@when('Enter email address in input and click arrow button')
def step_impl(context):
    context.page.subscribe(context.config.userdata['email'])


@then('Verify success message "You have been successfully subscribed!" is visible')
def step_impl(context):
    context.page.verify_success_message()