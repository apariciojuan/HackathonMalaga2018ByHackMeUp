import unittest
import os
import subprocess

class TestExercise(unittest.TestCase):

    def test_case1(self):
        user_input = "4 3\n2 4\n6\nup\nright\nright\ndown\ndown\nleft"
        expected_output = "YOU WIN!"
        with os.popen("echo '" + user_input + "' | python3 exercise09_pacman.py") as o:
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
        user_input = "4 3\n4 4\n5\nright\nright\ndown\ndown\ndown"
        expected_output = "YOU LOSE!"
        with os.popen("echo '" + user_input + "' | python3 exercise09_pacman.py") as o:
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
        user_input = "4 3\n4 4\n3\nright\nright\ndown"
        expected_output = "YOU WIN!"
        with os.popen("echo '" + user_input + "' | python3 exercise09_pacman.py") as o:
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

    def test_case4(self):
        user_input = "4 2\n5 5\n4\nup\nup\nup\nup"
        expected_output = "YOU ARE EVEN!"
        with os.popen("echo '" + user_input + "' | python3 exercise09_pacman.py") as o:
            output = o.read()
        output = output.strip() # Remove leading spaces and LFs

        print("\n\nTEST CASE 4")
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
