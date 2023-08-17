import unittest

import HtmlTestRunner

from test_cases.TestNegativeLogin import TestNegativeLogin
from test_cases.TestPositiveLogin import TestPositiveLogin


class TestSuite(unittest.TestCase):

    def tests_suite(self):
        tests_suite = unittest.TestSuite()
        tests_suite.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(TestPositiveLogin),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestNegativeLogin)
        ])
        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,
            report_title="Positive and Negative Login for https://practicetestautomation.com/practice-test-login/",
            report_name="Test Results",
        )
        runner.run(tests_suite)