import os
import sys
import unittest
from day06_part02 import build_passengers_from_file


class TestDay06Part01(unittest.TestCase):
    def test_sample01(self):
        #Arrange
        file_path = os.path.join(sys.path[0], "input_sample01.txt")

        # Act
        passenger_groups = build_passengers_from_file(file_path)
        total_common_answers = [answer for group in passenger_groups for common_answers in group.get_common_answers()
                                for answer in common_answers]

        # Assert
        self.assertEqual(len(total_common_answers), 6)


if __name__ == '__main__':
    unittest.main()