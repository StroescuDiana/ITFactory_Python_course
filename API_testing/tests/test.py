import unittest

from api_requests.simple_books_request import get_status, submit_order


class ApiTestCase(unittest.TestCase):

    def test_status(self):
        response = get_status()
        assert response == "OK"

    def test_submit_order(self):
        response = submit_order()
        assert response == True