"""
    https://realpython.com/python-mock-library
"""

import requests
import unittest
from unittest.mock import Mock

requests = Mock()


def get_holidays():
    r = requests.get("http://localhost/api/holidays")
    if r.status_code == 200:
        return r.json()
    return None


class TestCalendar(unittest.TestCase):
    def log_request(self, url):

        # Log a fake request for test output purposes

        print("The requested URL is {}".format(url))
        print("Request received")

        # Create a new Mock to imitate a Response
        response_mock = Mock()
        response_mock.status_code = 200
        response_mock.json.return_value = {
            "12/25": "Christmas",
            "7/4": "Independence Day",
        }
        return response_mock

    def test_get_holidays_logging(self):
        # Test a successful, logged request
        requests.get.side_effect = self.log_request
        assert get_holidays()["12/25"] == "Christmas"


if __name__ == "__main__":
    unittest.main()


# Instead of writing the above __name__ block, we can run the test cases with below command
# python -m unittest mocking_request
