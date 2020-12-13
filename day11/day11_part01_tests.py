import os
import sys
import unittest

from day11_common import build_seat_map_from_file, perform_steps_until_no_change, count_cells_with_value, \
    get_adjacent_seats


class TestDay11Part01(unittest.TestCase):
    def test_part01(self):
        # Arrange
        file_path = os.path.join(sys.path[0], "input_sample01.txt")
        initial_seat_map = build_seat_map_from_file(file_path)

        # Act
        result_seat_map, num_steps = perform_steps_until_no_change(initial_seat_map, get_adjacent_seats, 4)
        occupied_count = count_cells_with_value(result_seat_map, '#')

        # Assert
        self.assertEqual(occupied_count, 37)


if __name__ == '__main__':
    unittest.main()
