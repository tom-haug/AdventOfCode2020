import os
import sys
import unittest
from day13_part01 import get_part01_result_from_file


class TestDay13Part01(unittest.TestCase):
    def test_part01(self):
        # Arrange
        file_path = os.path.join(sys.path[0], "input_sample01.txt")

        # Act
        result = get_part01_result_from_file(file_path)

        # Assert
        self.assertEqual(result, 295)


if __name__ == '__main__':
    unittest.main()