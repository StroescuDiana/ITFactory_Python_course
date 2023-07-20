# Behavior-Driven Development

## Understanding BDD:
a. **What is BDD?** - Introduce the concept of Behavior-Driven Development and its focus on collaboration, communication, and shared understanding between stakeholders.

Behavior-Driven Development (BDD) is a software development process that revolves around producing tests that describe desired software behaviors.

The goal is to facilitate collaboration between business stakeholders, developers and testers by focusing on the behavior of the software. 
It helps ensure the team is building the right product, not just building the product right.

b. **Core Principles of BDD** - Explain the core principles of BDD, such as ubiquitous language, executable specifications, and the three amigos.

- `Ubiquitous Language`: Using a common vocabulary across the team to describe features. This helps align business needs with technical specifications.

- `Executable Specifications`: Writing examples (test cases) that describe how the software should behave. These examples are then automated to ensure features meet requirements.

- `The Three Amigos`: Involving business stakeholders, developers and testers together in discussions to clarify requirements and produce examples/tests.

c. **Benefits of BDD in Automation Testing** - Highlight the advantages of BDD in automation testing, including improved communication, test clarity, and maintainability.

- `Improved Communication`: The examples written in a business-readable format (Gherkin) improve communication between different roles.

- `Test Clarity`: The examples clearly define expected behaviors, making tests self-documenting and easier to understand.

- `Maintainability`: Examples endure for longer than code and can outlive specific implementations, improving test longevity.

- `Living Documentation`: The examples act as a documentation of desired behaviors and requirements, and evolve with the product.

- `Productivity`: BDD forces development of testable code, improving design for testability and maintainability.



## BDD Frameworks:
a. **Introduction to Cucumber** - Introduce Cucumber, a popular BDD framework that promotes collaboration and provides a structure for writing BDD-style tests.

`Cucumber` is a popular `BDD framework` that uses the Gherkin language to write `human-readable` specifications. It allows teams to collaborate and develop software that truly satisfies business requirements.

`Cucumber` `executes` Gherkin features (tests) that are linked to step definitions written in the development language (Ruby, Java, Python, etc.). 
This allows separating business logic from technical details and ensures a ubiquitous language across the team.

b. **Gherkin Syntax** - Explain the Gherkin syntax, which is used to write feature files in a human-readable format.

Gherkin uses a simple syntax consisting of:

- **Features**: Represent a requirement or piece of functionality
- **Scenarios**: Represent concrete examples or test cases within a Feature
- **Steps**: Represent individual actions in a Scenario

```text
Feature: Login
  Scenario: Login success
    Given I am on the login page   
    When I enter a valid username and password
    Then I should see a successful login message
```

c. **Setting up the Environment** - Guide participants through the installation and setup of Cucumber and necessary dependencies.

The setup steps to use `Cucumber` and `Gherkin`:

Python: Install Cucumber and selenium. Create features/ and step_definitions/ folders. Write a feature file and steps.py file with step definitions. Run using behave.

Cucumber then parses these Gherkin scenarios and maps each step to a step definition, written in the testing framework's language. For example:

```python
from selenium import webdriver

@given('I am on the login page') 
def go_to_login_page(context):
    # Initialize browser
    context.driver = webdriver.Chrome()
    
    # Navigate to login page    
    context.driver.get('http://example.com/login')

@when('I enter a valid username and password')  
def enter_credentials(context):
    # Find username and password fields   
    username = context.driver.find_element_by_id('username')
    password = context.driver.find_element_by_id('password')

    # Enter credentials     
    username.send_keys('valid_user')
    password.send_keys('valid_pass')

@when('I enter an invalid username and valid password')    
def enter_invalid_credentials(context):
    # Enter invalid username and valid password

@then('I should see a successful login message')
def check_success_message(context):
    # Find success message  
    success = context.driver.find_element_by_class_name('success')
    
    # Verify message is displayed
    assert success.is_displayed(), 'Success message not displayed'

@then('I should see an error message')    
def check_error_message(context):
    # Find and verify error message

def after_all(context):
    # Close browser  
    context.driver.quit()
```

Conclusion:

- Gherkin is the language used to write Cucumber scenarios, using features, scenarios and steps.

- Gherkin is a general behavior-driven development language, not specific to Cucumber.

- Cucumber parses Gherkin scenarios and maps steps to step definitions, written in your testing framework's language.

- The combination of Gherkin scenarios and step definitions allows Cucumber to automate acceptance tests.

So while Gherkin and Cucumber are separate things, they work together to enable Behavior Driven Development and write business-readable automated tests.

Testing scenarious using `Gherkin`:

```text
Feature: Login functionality

  @unit
  Scenario: Username validation 
    Given a username string
    When I validate the username 
    Then it should return "valid" or "invalid"

  @unit
  Scenario: Password validation
    Given a password string
    When I validate the password 
    Then it should return "valid" or "invalid"
    
  @integration    
  Scenario: Database connection
    Given the database details  
    When I connect to the database 
    Then the connection should be successful
    
  @integration  
  Scenario: Login API call
    Given a valid set of login details
    When I call the login API 
    Then I receive a success response
    
  @e2e
  Scenario: Login page title    
    Given I am on the login page
    When I verify the page title
    Then it should match "Login - My Website"
    
  @e2e   
  Scenario: Login success 
    Given I am on the login page
    When I enter valid credentials 
    And I click the login button   
    Then I should see a successful login message
```

This covers:

- Unit testing scenarios - validating inputs
- Integration testing scenarios - testing API calls and database connection
- End-to-end testing scenarios - testing actual login flow

The tags:
- `@unit` - for unit test scenarios
- `@integration` - for integration test scenarios
- `@e2e` - for end-to-end test scenarios

So running:

- `behave -t @unit` will run just the unit tests
- `behave -t @e2e` will run just the end-to-end tests
- `behave (with no tags)` will run all scenarios

Common tags that many teams use are:

- `@smoke` for smoke tests
- `@regression` for regression tests
- `@functional` for functional tests
- `@ui` for UI tests
- `@api` for API tests
- `@sanity` for sanity checks


## Writing BDD-style Automation Tests:
a. Identifying Scenarios and Features - Explain how to identify scenarios and features from requirements or user stories.

- Read through requirements and user stories
- Identify distinct user tasks and goals - these become scenarios
- Group related scenarios into features based on functionality
- Write a descriptive title for each feature

b. Writing Feature Files - Guide participants on writing feature files using Gherkin syntax, including defining scenarios, scenario outlines, and scenario steps.

- Start each feature with the title:
```text
- Feature: Login functionality
```

Add scenarios:
```text
Scenario: Login success
```

Add steps:
```text
Given I am on the login page  
When I enter valid credentials
Then I should see a success message
```

c. Implementing Step Definitions - Demonstrate how to implement step definitions in Python, mapping the Gherkin steps to automation code using Selenium and Python.

- Create a Python file for step definitions
- Add a step definition for each step:
```python
@given('I am on the login page')
def go_to_login_page(context):
   # Code to navigate to page
```
- Implement the logic using Selenium and Python

d. Executing BDD Tests - Show how to execute BDD tests using the Cucumber framework and generate human-readable reports.

Install behave: `pip install behave`

Run tests: `behave features/login.feature`
Cucumber will:
- Parse the feature file
- Match steps to step definitions
- Run the Python code
- Fail or pass scenarios
- Generate reports using:
`behave --outfile=report.html features/login.feature`

## Best Practices for BDD Automation Testing:
a. Collaborating with Stakeholders - Highlight the importance of involving stakeholders in the BDD process and fostering effective communication.
b. Keeping Scenarios Atomic and Independent - Explain the significance of atomic and independent scenarios for better test maintainability and reusability.
c. Writing Readable and Maintainable Step Definitions - Provide guidelines for writing clear, concise, and reusable step definitions.
d. Regularly Reviewing and Refactoring Feature Files - Emphasize the importance of reviewing and refactoring feature files to keep them up to date and maintainable.

## BDD Integration with Selenium and Python:
a. Setting up Selenium with Python - Assist participants in setting up Selenium WebDriver with Python for web automation testing.
```bash
pip install selenium

# Install a browser driver - ChromeDriver in this case
pip install selenium-chromedriver
```

In your test code:

```python
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://www.google.com')
```

b. Writing BDD-style Tests with Selenium and Python - Demonstrate how to combine Selenium and Python to write BDD-style tests using Gherkin syntax and step definitions.

features/search.feature:

```text
Feature: Google Search

Scenario: Search for a query  
  Given I am on Google's homepage      
  When I search for "Selenium Python" 
  Then I see search results
```

step_definitions/search_steps.py:

```python
@given('I am on Google's homepage')
def go_to_google(context):
   driver = context.driver  
   driver.get('http://www.google.com')

@when('I search for "{query}"')    
def search(context, query):
    # Enter query and submit form

@then('I see search results')
def see_results(context):
    # Verify search results are displayed
```

c. Running BDD Tests using the Selenium-Python Framework - Guide participants on executing BDD tests using the Selenium-Python framework and generating meaningful reports.

```python
from behave import *

# Initialize the driver in a before_all hook
@before_all
def setup(context):
    context.driver = webdriver.Chrome()

# Quit the driver in an after_all hook   
@after_all    
def teardown(context): 
    context.driver.quit()

if __name__ == '__main__':
    behave features/
```

This will:

- Initialize the Selenium driver
- Parse the Gherkin feature file
- Run the step definitions by matching steps
- Fail or pass scenarios
- Quit the driver after all tests finish
