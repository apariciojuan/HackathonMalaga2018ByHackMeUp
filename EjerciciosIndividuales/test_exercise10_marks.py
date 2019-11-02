import unittest
import os
import subprocess

class TestExercise(unittest.TestCase):

    def test_case1(self):
        user_input = "5 3\n8.9 9 7.8 9.3 8\n9 9.1 8.5 8.8 8.6\n9.1 9.2 8.3 8.9 9.05"
        expected_output = "9.00\n9.10\n8.20\n9.00\n8.55"
        with os.popen("echo '" + user_input + "' | python3 exercise10_marks.py") as o:
            output = o.read()
        output = output.strip() # Remove leading spaces and LFs

        print("\n\nTEST CASE 1")
        print("===========")
        print("\nInput:")
        print(user_input)
        print("\nOutput:")
        print(output)
        print("\nExpected output:")
        print(expected_output)
        print("")
        self.assertEqual(output, expected_output)

    def test_case2(self):
        user_input = "4 3\n7.5 9 7.8 6\n9 9.1 10 6.5\n8 9 8 9\n"
        expected_output = "8.17\n9.03\n8.60\n7.17"
        with os.popen("echo '" + user_input + "' | python3 exercise10_marks.py") as o:
            output = o.read()
        output = output.strip() # Remove leading spaces and LFs

        print("\n\nTEST CASE 2")
        print("===========")
        print("\nInput:")
        print(user_input)
        print("\nOutput:")
        print(output)
        print("\nExpected output:")
        print(expected_output)
        print("")
        self.assertEqual(output, expected_output)

    def test_case3(self):
        user_input = "6 2\n7.5 9 7.8 6 8.75 5.25\n9 9.1 10 6.5 8 9"
        expected_output = "8.25\n9.05\n8.90\n6.25\n8.38\n7.12"
        with os.popen("echo '" + user_input + "' | python3 exercise10_marks.py") as o:
            output = o.read()
        output = output.strip() # Remove leading spaces and LFs

        print("\n\nTEST CASE 3")
        print("===========")
        print("\nInput:")
        print(user_input)
        print("\nOutput:")
        print(output)
        print("\nExpected output:")
        print(expected_output)
        print("")
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main()
