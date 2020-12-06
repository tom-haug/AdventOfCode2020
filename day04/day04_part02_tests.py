import os
import sys
import unittest
from day04 import day04_common


class TestDay04Part02(unittest.TestCase):
    def test_all_invalid(self):
        # Arrange
        file_path = os.path.join(sys.path[0], "input_strict_all_invalid.txt")
        rules = day04_common.strict_password_rules()

        # Act
        count = day04_common.get_valid_passport_count(file_path, rules)

        # Assert
        self.assertEqual(count, 0)

    def test_all_valid(self):
        # Arrange
        file_path = os.path.join(sys.path[0], "input_strict_all_valid.txt")
        rules = day04_common.strict_password_rules()

        # Act
        count = day04_common.get_valid_passport_count(file_path, rules)

        # Assert
        self.assertEqual(count, 4)


if __name__ == '__main__':
    unittest.main()
