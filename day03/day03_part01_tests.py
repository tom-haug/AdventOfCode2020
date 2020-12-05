import os
import sys
import unittest
import day03_part01


class TestDay03Part01(unittest.TestCase):
    def test_sample1(self):
        #Arrange
        file_path = os.path.join(sys.path[0], "input_sample01.txt")

        #Act
        tree_count = day03_part01.get_tree_count(file_path)

        #Assert
        self.assertEqual(tree_count, 7)


if __name__ == '__main__':
    unittest.main()