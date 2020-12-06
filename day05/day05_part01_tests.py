import os
import sys
import unittest
from day05_common import build_boarding_pass_list_from_file, get_max_seat_boarding_pass


class TestDay05Part01(unittest.TestCase):
    def test_sample1(self):
        # Arrange
        file_path = os.path.join(sys.path[0], "input_sample01.txt")
        airplane_rows = 128

        # Act
        boarding_passes = build_boarding_pass_list_from_file(file_path, airplane_rows)
        max_seat_boarding_pass = get_max_seat_boarding_pass(boarding_passes)

        # Assert
        self.assertEqual(max_seat_boarding_pass.seat_id(), 820)


if __name__ == '__main__':
    unittest.main()
