import unittest
import os
import subprocess

class TestExercise(unittest.TestCase):

    def test_case1(self):
        input = "5"
        expected_output = "--------e--------\n------e-d-e------\n----e-d-c-d-e----\n--e-d-c-b-c-d-e--\ne-d-c-b-a-b-c-d-e\n--e-d-c-b-c-d-e--\n----e-d-c-d-e----\n------e-d-e------\n--------e--------"
        with os.popen("echo '" + input + "' | python3 exercise03_tapestry.py") as o:
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
        input = "7"
        expected_output = "------------g------------\n----------g-f-g----------\n--------g-f-e-f-g--------\n------g-f-e-d-e-f-g------\n----g-f-e-d-c-d-e-f-g----\n--g-f-e-d-c-b-c-d-e-f-g--\ng-f-e-d-c-b-a-b-c-d-e-f-g\n--g-f-e-d-c-b-c-d-e-f-g--\n----g-f-e-d-c-d-e-f-g----\n------g-f-e-d-e-f-g------\n--------g-f-e-f-g--------\n----------g-f-g----------\n------------g------------"
        with os.popen("echo '" + input + "' | python3 exercise03_tapestry.py") as o:
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
        expected_output = "--b--\nb-a-b\n--b--"
        with os.popen("echo '" + input + "' | python3 exercise03_tapestry.py") as o:
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
        input = "3"
        expected_output = "----c----\n--c-b-c--\nc-b-a-b-c\n--c-b-c--\n----c----"
        with os.popen("echo '" + input + "' | python3 exercise03_tapestry.py") as o:
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
