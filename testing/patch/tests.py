import unittest
from my_calendar import get_holidays, requests
from requests.exceptions import Timeout
from unittest.mock import patch

# class TestCalendar(unittest.TestCase):
#     @patch('my_calendar.requests')
#     def test_get_holidays_timeout(self, mock_requests):
#             mock_requests.get.side_effect = Timeout
#             with self.assertRaises(Timeout):
#                 get_holidays()
#                 mock_requests.get.assert_called_once()


"""
    Patch as a context manager.
    1. You only want to mock an object for a part of the test scope.
    2. You are already using too many decorators or parameters, which hurts your test’s readability.
"""


# class TestCalendar(unittest.TestCase):
#     def test_get_holidays_timeout(self):
#         with patch('my_calendar.requests') as mock_requests:
#             mock_requests.get.side_effect = Timeout
#             with self.assertRaises(Timeout):
#                 get_holidays()
#                 mock_requests.get.assert_called_once()


class TestCalendar(unittest.TestCase):
    @patch.object(requests, "get", side_effect=requests.exceptions.Timeout)
    def test_get_holidays_timeout(self, mock_requests):
        with self.assertRaises(requests.exceptions.Timeout):
            get_holidays()


if __name__ == "__main__":
    unittest.main()
