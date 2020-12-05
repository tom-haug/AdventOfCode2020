import os
import sys
import unittest
import day03_part02


class TestDay03Part02(unittest.TestCase):
    def test_sample1(self):
        #Arrange
        file_path = os.path.join(sys.path[0], "input_sample01.txt")
        slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

        #Act
        total = day03_part02.get_multiplied_tree_counts(file_path, slopes)

        #Assert
        self.assertEqual(total, 336)


if __name__ == '__main__':
    unittest.main()