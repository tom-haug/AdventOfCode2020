import os
import sys
import pandas as pd

from day11_common import build_seat_map_from_file, perform_steps_until_no_change, count_cells_with_value, \
    get_adjacent_seats

if __name__ == '__main__':
    file_path = os.path.join(sys.path[0], "input.txt")
    initial_seat_map = build_seat_map_from_file(file_path)

    result_seat_map, num_steps = perform_steps_until_no_change(initial_seat_map, get_adjacent_seats, 4)
    occupied_count = count_cells_with_value(result_seat_map, '#')

    print('initial')
    print(initial_seat_map)
    print('result_seat_map 1')
    print(result_seat_map)
    print('num_steps', num_steps)
    print('occupied_count', occupied_count)
