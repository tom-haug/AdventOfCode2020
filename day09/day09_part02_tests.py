import os
import sys
import unittest

from day09_common import load_number_list_from_file, find_encryption_weakness_from_initial_input


class TestDay09Part02(unittest.TestCase):
    def test_sample02(self):
        # Arrange
        file_path = os.path.join(sys.path[0], 'input_sample01.txt')
        num_list = load_number_list_from_file(file_path)
        check_item_count = 5

        # Act
        encryption_weakness = find_encryption_weakness_from_initial_input(num_list, check_item_count)

        # Assert
        self.assertEqual(encryption_weakness, 62)


if __name__ == '__main__':
    unittest.main()
