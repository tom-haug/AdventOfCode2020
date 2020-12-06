import os
import sys
from day02 import day02_part02
import unittest


class TestDay02PartO2(unittest.TestCase):
    def test_sample1(self):
        # Arrange
        file_path = os.path.join(sys.path[0], "input_sample01.txt")

        # Act
        password_count = day02_part02.get_valid_password_count(file_path)

        # Assert
        self.assertEqual(password_count, 1)


if __name__ == '__main__':
    unittest.main();
