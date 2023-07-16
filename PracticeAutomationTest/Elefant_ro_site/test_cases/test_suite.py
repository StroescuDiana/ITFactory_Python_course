import unittest

import HtmlTestRunner

from Elefant_ro_site.test_cases.test_positive_exercises import TestPositive
from Elefant_ro_site.test_cases.test_negative_exercises import TestNegative


class TestSuite(unittest.TestCase):

    def tests_suite(self):
        tests_suite = unittest.TestSuite()
        tests_suite.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(TestPositive),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestNegative)
        ])
        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,
            report_title="Login Page Test Report",
            report_name="Test Results",
        )
        runner.run(tests_suite)