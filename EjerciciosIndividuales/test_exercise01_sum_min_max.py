import unittest
import os
import subprocess

class TestExercise(unittest.TestCase):

    def test_case1(self):
        input = "20 11 20 33 18 5 24 42"
        expected_output = "173\n5\n42"
        with os.popen("echo '" + input + "' | python3 exercise01_sum_min_max.py") as o:
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
        input = "17 3 5 80"
        expected_output = "105\n3\n80"
        with os.popen("echo '" + input + "' | python3 exercise01_sum_min_max.py") as o:
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
        input = "10 10 10 10"
        expected_output = "40\n10\n10"
        with os.popen("echo '" + input + "' | python3 exercise01_sum_min_max.py") as o:
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
        input = "1024"
        expected_output = "1024\n1024\n1024"
        with os.popen("echo '" + input + "' | python3 exercise01_sum_min_max.py") as o:
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
