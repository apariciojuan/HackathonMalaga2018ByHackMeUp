import unittest
import os
import subprocess

class TestExercise(unittest.TestCase):

    def test_case1(self):
        user_input = "9\nBANANA FRIES 12\nPOTATO CHIPS 30\nAPPLE JUICE 10\nCANDY 5\nAPPLE JUICE 10\nCANDY 5\nCANDY 5\nCANDY 5\nPOTATO CHIPS 30"
        expected_output = "BANANA FRIES 12\nPOTATO CHIPS 60\nAPPLE JUICE 20\nCANDY 20"
        with os.popen("echo '" + user_input + "' | python3 exercise11_supermarket.py") as o:
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
        user_input = "6\nBEANS 4\nDARK CHOCOLATE 7\nDARK CHOCOLATE 7\nCOCONUT 20\nBEANS 4\nBEANS 4"
        expected_output = "BEANS 12\nDARK CHOCOLATE 14\nCOCONUT 20"
        with os.popen("echo '" + user_input + "' | python3 exercise11_supermarket.py") as o:
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


if __name__ == '__main__':
    unittest.main()
