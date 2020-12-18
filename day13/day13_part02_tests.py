import os
import sys
import unittest

from day13_common import build_bus_schedules_from_file, get_base_time_for_bus_offsets


class TestDay13Part02(unittest.TestCase):
    param_list = [('input_sample01.txt', 1068781),
                  ('input_sample02.txt', 3417),
                  ('input_sample03.txt', 754018),
                  ('input_sample04.txt', 779210),
                  ('input_sample05.txt', 1261476),
                  ('input_sample06.txt', 1202161486)]

    def test_all_inputs(self):
        for file_name, expected_total_count in self.param_list:
            with self.subTest(file_name):
                self._test_part02(file_name, expected_total_count)

    def _test_part02(self, file_name: str, expected_result: int):
        #Arrange
        file_path = os.path.join(sys.path[0], file_name)

        #Act
        buses, initial_time = build_bus_schedules_from_file(file_path)
        base_time = get_base_time_for_bus_offsets(buses)

        #Assert
        self.assertEqual(base_time, expected_result)


if __name__ == '__main__':
    unittest.main()