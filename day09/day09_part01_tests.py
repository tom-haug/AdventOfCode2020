import os
import sys
import unittest

from day09_common import load_number_list_from_file, find_first_invalid_num


class TestDay09Part01(unittest.TestCase):

    def test_sample01(self):
        # Arrange
        file_path = os.path.join(sys.path[0], 'input_sample01.txt')
        num_list = load_number_list_from_file(file_path)
        check_item_count = 5

        # Act
        first_invalid_num = find_first_invalid_num(num_list, check_item_count)

        # Assert
        self.assertEqual(first_invalid_num, 127)


if __name__ == '__main__':
    unittest.main()
