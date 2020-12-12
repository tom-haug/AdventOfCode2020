import os
import sys
import unittest
from day07_common import build_bags_from_file


class TestDay07Part02(unittest.TestCase):
    param_list = [('input_sample01.txt', 32), ('input_sample02.txt', 126)]

    def test_all_inputs(self):
        for file_name, expected_total_count in self.param_list:
            with self.subTest(file_name):
                self._test_sample01(file_name, expected_total_count)

    def _test_part02(self, file_name, expected_total_count):
        print('testing ' + file_name)
        #Arrange
        file_path = os.path.join(sys.path[0], file_name)
        search_bag = 'shiny gold'
        bags = build_bags_from_file(file_path)
        shiney_gold_bag = next((bag for bag in bags if bag.bag_name == search_bag), None)

        # Act
        total_count = shiney_gold_bag.count_bags_recursive() - 1

        # Assert
        self.assertEqual(total_count, expected_total_count)


if __name__ == '__main__':
    unittest.main()