import unittest

from day15_part01 import get_next_number, play_game


class TestDay14(unittest.TestCase):
    def test_part01(self):
        param_list = [('0,3,6', 436),
                      ('1,3,2', 1),
                      ('2,1,3', 10),
                      ('1,2,3', 27),
                      ('2,3,1', 78),
                      ('3,2,1', 438),
                      ('3,1,2', 1836)]
        num_turns = 2020
        for initial_values, expected_result in param_list:
            self._test_part01(initial_values, num_turns, expected_result)

    def _test_part01(self, initial_values: str, num_turns: int, expected_result: int):
        # Arrange

        # Act
        spoken_numbers = play_game(initial_values, num_turns)

        # Assert
        self.assertEqual(len(spoken_numbers), num_turns)
        self.assertEqual(spoken_numbers[-1], expected_result)


if __name__ == '__main__':
    unittest.main()
