import unittest

import HtmlTestRunner

from Practice_test_automation_site.test_cases.test_positive_login import TestPositiveLogin
from Practice_test_automation_site.test_cases.test_negative_login import TestNegativeLogin


class TestSuite(unittest.TestCase):

    def tests_suite(self):
        tests_suite = unittest.TestSuite()
        tests_suite.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(TestPositiveLogin),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestNegativeLogin)
        ])
        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,
            report_title="Login Page Test Report",
            report_name="Test Results"
        )
        runner.run(tests_suite)
