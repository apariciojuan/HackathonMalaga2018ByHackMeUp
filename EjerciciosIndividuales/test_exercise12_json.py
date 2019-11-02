import unittest
import os
import subprocess

class TestExercise(unittest.TestCase):

    def test_case1(self):
        user_input = ""
        expected_output = "BWF678"
        with os.popen("echo '" + user_input + "' | python3 exercise12_json.py") as o:
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

if __name__ == '__main__':
    unittest.main()
