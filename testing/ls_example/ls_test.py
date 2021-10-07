"""
    mock.patch('package.module.className')
    mock.patch('package.module.className.function_name')
    mock.patch('package.module.function_name')
    mock.patch('package.module.className', return_value="abc")
    mock.patch('package.module.className', side_effect=Exception("boom!"))

    We mock the function where it has been used, not where it has been defined.

    Ways to apply the mock:-
        1. Decorator
        2. Context Manager
        3. Inline
"""

import unittest
from ls import LsContent
from unittest import mock, TestCase

class TestExamples(TestCase):
    # def test_print_contents_of_cwd_one(self):
    #     actual_result = LsContent().calc()
    #     expected_res = 10

    #     self.assertEqual(expected_res, actual_result)


    @mock.patch('ls.LsContent.add', return_value=15)
    def test_print_contents_of_cwd_two(self, mock_check_output):
        actual_result = LsContent().calc()
        expected_dir = 15

        self.assertEqual(expected_dir, actual_result)


    def test_print_contents_of_cwd_three(self):
        with mock.patch('ls.LsContent.add', return_value=20):
            actual_result = LsContent().calc()
        
        expected_dir = 20
        self.assertEqual(expected_dir, actual_result)



""" Inline method of patching or mocking """

# class TestExamplesInline(TestCase):

#     def setUp(self) -> None:
#         self.patcher = mock.patch('ls.check_output', return_value=b"foo\nbar\n")
#         self.patcher.start()

    
#     def test_print_contents_of_cwd_one(self):
#         actual_result = ls.print_contents_of_cwd()
#         expected_dir = b'foo'

#         self.assertIn(expected_dir, actual_result)

    
#     def tearDown(self) -> None:
#         self.patcher.stop()


if __name__== "__main__":
    unittest.main()
