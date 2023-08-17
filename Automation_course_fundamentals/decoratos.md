# Decorators
A list of decorators as an introduction. This list is of course just an overview of some important decorators. The most important are the decorators We are learning in our course. This is only an extension for the curious minds.

- `@classmethod` - Converts a method into a class method.
- `@staticmethod` - Converts a method into a static method.
- `@property` - Converts a method into a property.
- `@abstractmethod` - Marks a method as abstract. Used for ABCs and abstract classes.
- `@override` - Checks if a method actually overrides a parent class method. Used for type checking.
- `@unittest.skip` - Skips the decorated test.
- `@unittest.skipIf` - Skips the decorated test if the condition evaluates to True.
- `@unittest.skipUnless` - Skips the decorated test unless the condition evaluates to True.
- `@unittest.expectedFailure` - Marks the test as an expected failure.
- `@pytest.fixture` - Marks a function as a fixture function.
- `@pytest.mark.parametrize` - Uses the fixture multiple times with the data specified.
- `@pytest.mark.skip` - Skip the test for the given version or condition.
- `@pytest.mark.slow` - Mark the test as slow so it is not run by default.
- `@pytest.mark.serial` - Force the test to run serially.
- `@lru_cache` - Caches the result of a function, avoiding recomputing it.
- `@timer` - Times the execution of a function.
- `@iterable` - Allows an iterable object to be used as a decorator, decorating every function in the iterable.
- `@cache` - Simple cache implementation. Caches the result of a function.
- `@contextmanager` - Allows you to implement a context manager.
- `@level` - Sets the log level for the function. Used to log debug statements.
- `@deprecate` - Deprecates a function and marks it for removal in a future version.
- `@functools.wraps` - Preserves the metadata of the wrapped function (name, doc, etc). Used when creating decorators.
- `@singledispatchmethod` - Enables generic single dispatch. Dispatches methods based on the type of the first argument.
- `@profile` - Runs the function through cProfile and prints profiling stats. Used for optimization.
- `@lambda` - Allows you to create lambda expressions as decorators.

Some example of how to use some decorators:

1. `@classmethod` (OOP):

**Description**: This decorator is used to define a class method in Python. A class method is a method that belongs to the class rather than an instance of the class.

```python
class MyClass:
    @classmethod
    def my_class_method(cls, arg1, arg2):
        # Code goes here
        pass
```

2. `@staticmethod` (OOP):

**Description**: This decorator is used to define a class method in Python. A class method is a method that belongs to the class rather than an instance of the class.

```python
class MyClass:
    @staticmethod
    def my_static_method(arg1, arg2):
        # Code goes here
        pass

```

3. `@property` (OOP):

**Description**: This decorator is used to define a property in Python. Properties allow you to define methods that can be accessed like attributes, providing control over the access and modification of class attributes.

```python
class MyClass:
    @property
    def my_property(self):
        return self._my_property

    @my_property.setter
    def my_property(self, value):
        self._my_property = value
```

4. `@pytest.fixture` (Automation Testing with pytest):

**Description**: This decorator is used in pytest to define a fixture, which is a function that provides a fixed baseline for tests. Fixtures can be used to set up preconditions or perform cleanup activities before and after tests.

```python
import pytest

@pytest.fixture
def setup_data():
    # Code to set up test data
    yield
    # Code to clean up after the test

def test_my_function(setup_data):
    # Test code that uses the setup_data fixture
    pass
```

5. `@pytest.mark.parametrize` (Automation Testing with pytest):

**Description**: This decorator is used to specify different sets of inputs for a test function in pytest. It allows you to run the same test code with multiple input values, making it easy to test a function with different scenarios.

```python
import pytest

@pytest.mark.parametrize("input, expected", [
    (2, 4),
    (3, 9),
    (4, 16),
])
def test_square(input, expected):
    assert input ** 2 == expected
```

6. `@pytest.mark.selenium` (Selenium Automation Testing with pytest):

**Description**: This decorator is used to mark a test function as a Selenium test in pytest. It is often used to distinguish Selenium tests from regular unit tests, enabling specific test configurations and behaviors for Selenium automation.

```python
import pytest

@pytest.mark.selenium
def test_login():
    # Code to automate login using Selenium
    pass
```

7. `@unittest.skip`:

**Description**: Skips the execution of a specific test function or class. This decorator is used when a test is not ready or temporarily disabled.

```python
import unittest

class MyTestCase(unittest.TestCase):
    @unittest.skip("Test is not yet implemented")
    def test_function(self):
        # Test code
        pass
```

8. `@unittest.skipIf`:

Description: Skips the execution of a specific test function or class based on a condition. It allows skipping tests under specific circumstances, such as skipping on certain platforms or for specific Python versions.

```python
import unittest
import sys

class MyTestCase(unittest.TestCase):
    @unittest.skipIf(sys.version_info < (3, 7), "Requires Python 3.7+")
    def test_function(self):
        # Test code
        pass
```

9. `@unittest.expectedFailure`:

**Description**: Marks a test function or class as an expected failure. If the test fails as expected, it won't be reported as a failure but as an expected failure.

```python
import unittest

class MyTestCase(unittest.TestCase):
    @unittest.expectedFailure
    def test_function(self):
        # Test code that is expected to fail
        pass
```

10. `@unittest.skipUnless`:

**Description**: Skips the execution of a specific test function or class unless a condition is met. It allows skipping tests unless specific criteria are fulfilled.

```python
import unittest

class MyTestCase(unittest.TestCase):
    @unittest.skipUnless(some_condition, "Skipping test unless condition is met")
    def test_function(self):
        # Test code
        pass
```

11.`@unittest.expectedWarning`:

**Description**: Marks a test function or class as an expected warning. If the test triggers an expected warning, it won't be reported as a failure but as an expected warning.

```python
import unittest

class MyTestCase(unittest.TestCase):
    @unittest.expectedWarning
    def test_function(self):
        # Test code that is expected to trigger a warning
        pass
```

More information can be found at the following links:

- https://realpython.com/primer-on-python-decorators/
- https://peps.python.org/pep-0318/
- https://wiki.python.org/moin/PythonDecorators
- https://www.programiz.com/python-programming/decorator
- https://github.com/lord63/awesome-python-decorator
