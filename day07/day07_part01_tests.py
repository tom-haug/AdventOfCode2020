import os
import sys
import unittest
from day07_common import build_bags_from_file


class TestDay07Part01(unittest.TestCase):
    def test_sample01(self):
        #Arrange
        file_path = os.path.join(sys.path[0], "input_sample01.txt")
        search_bag = 'shiny gold'

        # Act
        bags = build_bags_from_file(file_path)
        result_bags = [bag for bag in bags if bag.can_eventually_contain(search_bag)]

        # Assert
        self.assertEqual(len(result_bags), 4)


if __name__ == '__main__':
    unittest.main()