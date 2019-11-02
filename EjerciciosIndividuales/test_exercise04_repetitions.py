import unittest
import os
import subprocess

class TestExercise(unittest.TestCase):

    def test_case1(self):
        input = "44488888904433300"
        expected_output = "(4, 3)\n(8, 5)\n(9, 1)\n(0, 1)\n(4, 2)\n(3, 3)\n(0, 2)"
        with os.popen("echo '" + input + "' | python3 exercise04_repetitions.py") as o:
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
        input = "6661234"
        expected_output = "(6, 3)\n(1, 1)\n(2, 1)\n(3, 1)\n(4, 1)"
        with os.popen("echo '" + input + "' | python3 exercise04_repetitions.py") as o:
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
        input = "2"
        expected_output = "(2, 1)"
        with os.popen("echo '" + input + "' | python3 exercise04_repetitions.py") as o:
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
        input = "000777"
        expected_output = "(0, 3)\n(7, 3)"
        with os.popen("echo '" + input + "' | python3 exercise04_repetitions.py") as o:
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
