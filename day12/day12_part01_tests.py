import os
import sys
import unittest

from day12_part01 import build_instructions_from_file, NavigationState, Point, Direction


class TestDay12Part01(unittest.TestCase):
    def test_part01(self):
        # Arrange
        file_path = os.path.join(sys.path[0], "input_sample01.txt")
        instructions = build_instructions_from_file(file_path)
        initial_nav_state = NavigationState(Point(0, 0), Direction.East)
        cur_nav_state = NavigationState(Point(0, 0), Direction.East)

        # Act
        for instruction in instructions:
            cur_nav_state = instruction.perform(cur_nav_state)
            print(cur_nav_state.direction)
            print(cur_nav_state.location)

        total_distance = cur_nav_state.location.manhatten_distance_from(initial_nav_state.location)

        # Assert
        self.assertEqual(total_distance, 25)


if __name__ == '__main__':
    unittest.main()
