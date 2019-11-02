import unittest
import os
import subprocess

class TestExercise(unittest.TestCase):

    def test_case1(self):
        input = "Hack me up!"
        expected_output = "acehkmpu\nac ae ah ak am ap au ce ch ck cm cp cu eh ek em ep eu hk hm hp hu km kp ku mp mu pu"
        with os.popen("echo '" + input + "' | python3 exercise05_combinations.py") as o:
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
        input = "I am a programmer."
        expected_output = "aegimopr\nae ag ai am ao ap ar eg ei em eo ep er gi gm go gp gr im io ip ir mo mp mr op or pr"
        with os.popen("echo '" + input + "' | python3 exercise05_combinations.py") as o:
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
        input = "hello world"
        expected_output = "dehlorw\nde dh dl do dr dw eh el eo er ew hl ho hr hw lo lr lw or ow rw"
        with os.popen("echo '" + input + "' | python3 exercise05_combinations.py") as o:
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
        input = "Oooohhhhhhhh!!!"
        expected_output = "ho\nho"
        with os.popen("echo '" + input + "' | python3 exercise05_combinations.py") as o:
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
