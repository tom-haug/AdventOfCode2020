import unittest

from day15_common import play_game


class TestDay15(unittest.TestCase):
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
            with self.subTest(f'initial_values: {initial_values}, num_turns: {num_turns}, expected_result: {str(expected_result)}'):
                self._run_test(initial_values, num_turns, expected_result)

    def test_part02(self):
        param_list = [('0,3,6', 175594),
                      ('1,3,2', 2578),
                      ('2,1,3', 3544142),
                      ('1,2,3', 261214),
                      ('2,3,1', 6895259),
                      ('3,2,1', 18),
                      ('3,1,2', 362)]
        num_turns = 30000000
        for initial_values, expected_result in param_list:
            with self.subTest(f'initial_values: {initial_values}, num_turns: {num_turns}, expected_result: {str(expected_result)}'):
                print('WARNING: long-running test!!', initial_values, num_turns)
                self._run_test(initial_values, num_turns, expected_result)

    def _run_test(self, initial_values: str, num_turns: int, expected_result: int):
        # Arrange

        # Act
        last_num_spoken = play_game(initial_values, num_turns)

        # Assert
        self.assertEqual(last_num_spoken, expected_result)


if __name__ == '__main__':
    unittest.main()
