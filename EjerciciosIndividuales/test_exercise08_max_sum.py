import unittest
import os
import subprocess

class TestExercise(unittest.TestCase):

    def test_case1(self):
        user_input = "5\n7 53 183 439 863\n497 383 563 79 973\n287 63  343 169 583\n627 343 773 959 943\n767 473 103 699 303"
        expected_output = "3315"
        with os.popen("echo '" + user_input + "' | python3 exercise08_max_sum.py") as o:
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
        user_input = "4\n1 2 3 4\n5 6 7 8\n9 0 1 2\n3 4 5 6"
        expected_output = "24"
        with os.popen("echo '" + user_input + "' | python3 exercise08_max_sum.py") as o:
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
        user_input = "6\n777 531 183 439 863 345\n497 383 563 792 973 919\n287 633 343 169 583 123\n627 343 773 959 943 427\n767 473 103 699 303 892\n679 380 212 533 623 785"
        expected_output = "4640"
        with os.popen("echo '" + user_input + "' | python3 exercise08_max_sum.py") as o:
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
