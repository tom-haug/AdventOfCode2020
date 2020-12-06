import os
import sys
import unittest
import day04_common


class TestDay04Part01(unittest.TestCase):
    def test_sample1(self):
        #Arrange
        file_path = os.path.join(sys.path[0], "input_sample01.txt")
        rules = day04_common.basic_password_rules()

        #Act
        count = day04_common.get_valid_passport_count(file_path, rules)

        #Assert
        self.assertEqual(count, 2)


if __name__ == '__main__':
    unittest.main()