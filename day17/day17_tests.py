import unittest
import numpy as np
from day17_common import load_pocket_dimension_from_file, perform_cycle


class TestDay17(unittest.TestCase):
    def _run_test(self, file_name: str, num_dimensions: int, num_cycles: int, expected_active_cubes: int):
        pocket_dimension = load_pocket_dimension_from_file(file_name, num_dimensions, num_cycles)

        for cur_cycle in range(num_cycles):
            pocket_dimension = perform_cycle(pocket_dimension)

        number_active_cubes = np.count_nonzero(pocket_dimension)
        self.assertEqual(number_active_cubes, expected_active_cubes)

    def test_part01(self):
        self._run_test(file_name='input_sample01.txt', num_dimensions=3, num_cycles=6, expected_active_cubes=112)

    def test_part02(self):
        self._run_test(file_name='input_sample01.txt', num_dimensions=4, num_cycles=6, expected_active_cubes=848)


if __name__ == '__main__':
    unittest.main()
