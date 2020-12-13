import os
import sys
import unittest

from day10_common import load_joltage_list_from_file, get_all_valid_adapter_combinations


class TestDay10Part01(unittest.TestCase):
    param_list = [('input_sample01.txt', 8), ('input_sample02.txt', 19208)]

    def test_all_inputs(self):
        for file_name, expected_result in self.param_list:
            with self.subTest(file_name):
                self._test_part02(file_name, expected_result)

    def _test_part02(self, file_name, expected_result):
        # Arrange
        file_path = os.path.join(sys.path[0], file_name)
        joltage_list = load_joltage_list_from_file(file_path)
        joltage_list.append(0)  # add the wall as a node

        # Act
        total_combinations = get_all_valid_adapter_combinations(joltage_list)

        # Assert
        self.assertEqual(total_combinations, expected_result)


if __name__ == '__main__':
    unittest.main()
