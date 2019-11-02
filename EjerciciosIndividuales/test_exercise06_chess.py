import unittest
import os
import subprocess

class TestExercise(unittest.TestCase):

    def test_case1(self):
        input = "b4 e3"
        expected_output = "f8 e7 d6 a5 c5 d5 f5 c4 g4 a3 c3 c2 d2 g2 d1 e1 f1"
        with os.popen("echo '" + input + "' | python3 exercise06_chess.py") as o:
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
        input = "a1 h1"
        expected_output = "h8 g7 f6 e5 d4 c3 g3 b2 f2"
        with os.popen("echo '" + input + "' | python3 exercise06_chess.py") as o:
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
        input = "d4 e4"
        expected_output = "h8 a7 g7 b6 d6 f6 c5 e5 g5 c3 e3 g3 b2 d2 f2 a1 g1"
        with os.popen("echo '" + input + "' | python3 exercise06_chess.py") as o:
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


if __name__ == '__main__':
    unittest.main()
