"""
    https://realpython.com/python-mock-library
"""

import calc
import unittest


class TestCalc(unittest.TestCase):

    # Any test case must begin with test_ else it wont be considered as a test

    @classmethod
    def setUpClass(cls) -> None:
        print("Runs only once before test cases begins")

    @classmethod
    def tearDownClass(cls) -> None:
        print("Runs only once after all test cases finish running")

    def setUp(self) -> None:
        """This fun. runs before running each test case."""
        print("set up before each test case")

    def tearDown(self) -> None:
        """This fun. runs after each test case finsh running."""
        print("tear down after each test case")

    def test_add(self):

        self.assertEqual(calc.add(2, 3), 5)
        self.assertEqual(calc.add(-1, 3), 2)
        self.assertEqual(calc.add(-2, -3), -5)

    def test_substract(self):

        self.assertEqual(calc.subtract(5, 3), 2)
        self.assertEqual(calc.subtract(-1, 3), -4)
        self.assertEqual(calc.subtract(-2, -3), 1)
        self.assertEqual(calc.subtract(2, 3), -1)

    def test_multiply(self):

        self.assertEqual(calc.multiply(2, 3), 6)
        self.assertEqual(calc.multiply(-1, 3), -3)
        self.assertEqual(calc.multiply(-5, -3), 15)

    def test_divide(self):

        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(-3, 1), -3)
        self.assertEqual(calc.divide(-3, -3), 1)
        self.assertEqual(calc.divide(5, 2), 2.5)

        self.assertRaises(ValueError, calc.divide, 10, 0)
        # self.assertRaises(ValueError, calc.divide, 10, 2)  # test case failed here, since ValueError is not raised by divide

        with self.assertRaises(ValueError):
            calc.divide(10, 0)  # value error will be rasied here.


if __name__ == "__main__":
    unittest.main()
