import os
import sys
import unittest
from day06.day06_part01 import build_passengers_from_file


class TestDay06Part01(unittest.TestCase):
    def test_sample01(self):
        #Arrange
        file_path = os.path.join(sys.path[0], "input_sample01.txt")

        # Act
        passenger_groups = build_passengers_from_file(file_path)
        total_unique_answers = [answer for group in passenger_groups for unique_answers in group.get_unique_answers()
                                for answer in unique_answers]
        self.assertEqual(len(total_unique_answers), 11)


if __name__ == '__main__':
    unittest.main()