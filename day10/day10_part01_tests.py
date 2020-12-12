import os
import sys
import unittest

from day10_part01 import load_joltage_list_from_file, get_part01_result_from_joltage_list


class TestDay10Part01(unittest.TestCase):
    param_list = [('input_sample01.txt', 35), ('input_sample02.txt', 220)]

    def test_all_inputs(self):
        for file_name, expected_result in self.param_list:
            with self.subTest(file_name):
                self._test_part01(file_name, expected_result)

    def _test_part01(self, file_name, expected_result):
        # Arrange
        file_path = os.path.join(sys.path[0], file_name)
        joltage_list = load_joltage_list_from_file(file_path)

        # Act
        result = get_part01_result_from_joltage_list(joltage_list)

        # Assert
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
