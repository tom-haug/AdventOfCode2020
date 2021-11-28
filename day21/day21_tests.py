import unittest

import day21_part01 as part01
import day21_part02 as part02

class TestDay21(unittest.TestCase):

    def test_part01(self):
        file_name = 'input_sample01.txt'
        result = part01.get_part01_result(file_name)
        self.assertEqual(result, 5)


    def test_part02(self):
        file_name = 'input_sample01.txt'
        result = part02.get_part02_result(file_name)
        self.assertEqual(result, "mxmxvkd,sqjhc,fvjkl")


if __name__ == '__main__':
    unittest.main()