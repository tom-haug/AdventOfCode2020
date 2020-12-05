import os
import sys
import unittest
import day02_part01


class TestDay02Part01(unittest.TestCase):
    def test_sample1(self):
        # Arrange
        file_path = os.path.join(sys.path[0], "input_sample01.txt")

        # Act
        password_count = day02_part01.get_valid_password_count(file_path)

        # Assert
        self.assertEqual(password_count, 2)


if __name__ == '__main__':
    unittest.main()
