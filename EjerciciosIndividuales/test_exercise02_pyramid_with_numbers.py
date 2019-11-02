import unittest
import os
import subprocess

class TestExercise(unittest.TestCase):

    def test_case1(self):
        input = "4"
        expected_output = "---1---\n--121--\n-12321-\n1234321"
        with os.popen("echo '" + input + "' | python3 exercise02_pyramid_with_numbers.py") as o:
            output = o.read()
        output = output.strip() # Remove leading spaces and LFs

        print("\n\nTEST CASE 1")
        print("===========")
        print("\nInput:")
        print(input)
        print("\nOutput:")
        print(output)
        print("\nExpected output:")
        print(expected_output)
        print("")
        self.assertEqual(output, expected_output)

    def test_case2(self):
        input = "2"
        expected_output = "-1-\n121"
        with os.popen("echo '" + input + "' | python3 exercise02_pyramid_with_numbers.py") as o:
            output = o.read()
        output = output.strip() # Remove leading spaces and LFs

        print("\n\nTEST CASE 2")
        print("===========")
        print("\nInput:")
        print(input)
        print("\nOutput:")
        print(output)
        print("\nExpected output:")
        print(expected_output)
        print("")
        self.assertEqual(output, expected_output)

    def test_case3(self):
        input = "1"
        expected_output = "1"
        with os.popen("echo '" + input + "' | python3 exercise02_pyramid_with_numbers.py") as o:
            output = o.read()
        output = output.strip() # Remove leading spaces and LFs

        print("\n\nTEST CASE 3")
        print("===========")
        print("\nInput:")
        print(input)
        print("\nOutput:")
        print(output)
        print("\nExpected output:")
        print(expected_output)
        print("")
        self.assertEqual(output, expected_output)

    def test_case4(self):
        input = "7"
        expected_output = "------1------\n-----121-----\n----12321----\n---1234321---\n--123454321--\n-12345654321-\n1234567654321"
        with os.popen("echo '" + input + "' | python3 exercise02_pyramid_with_numbers.py") as o:
            output = o.read()
        output = output.strip() # Remove leading spaces and LFs

        print("\n\nTEST CASE 4")
        print("===========")
        print("\nInput:")
        print(input)
        print("\nOutput:")
        print(output)
        print("\nExpected output:")
        print(expected_output)
        print("")
        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()
