import unittest
import os
import subprocess

class TestExercise(unittest.TestCase):

    def test_case1(self):
        user_input = "4\n1\n1 2 3 4\n5 6 7 8\n9 0 1 2\n3 4 5 6"
        expected_output = "5 1 2 3\n9 0 6 4\n3 1 7 8\n4 5 6 2"
        with os.popen("echo '" + user_input + "' | python3 exercise07_array.py") as o:
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
        user_input = "5\n2\n11 22 33 44 0\n5 62 71 85 10\n91 0 11 24 16\n3 84 95 6 12\n13 14 5 16 17"
        expected_output = "91 5 11 22 33\n3 84 0 62 44\n13 95 11 71 0\n14 6 24 85 10\n5 16 17 12 16"
        with os.popen("echo '" + user_input + "' | python3 exercise07_array.py") as o:
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
        user_input = "3\n8\n1 2 3\n4 5 6\n7 8 9"
        expected_output = "1 2 3\n4 5 6\n7 8 9"
        with os.popen("echo '" + user_input + "' | python3 exercise07_array.py") as o:
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
