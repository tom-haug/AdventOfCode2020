import os
import sys
import numpy as np
from typing import Optional
np.set_printoptions(threshold=sys.maxsize)


def load_pocket_dimension_from_file(file_name: str, total_dimensions: int, padding_all_directions: int):
    file_path = os.path.join(sys.path[0], file_name)
    f = open(file_path, "r")
    input_lines = f.read().splitlines()
    f.close()

    initial_y_len = len(input_lines)
    initial_x_len = len(input_lines[0])

    padded_y_len = initial_y_len + 2 * padding_all_directions
    padded_x_len = initial_x_len + 2 * padding_all_directions

    array_dimensions = (padded_y_len, padded_x_len)

    additional_dimensions = total_dimensions - 2
    for cur_dimension in range(additional_dimensions):
        array_dimensions = (1 + 2 * padding_all_directions,) + array_dimensions

    pocket_dimension = np.zeros(array_dimensions, np.int)

    for y in range(len(input_lines)):
        line = input_lines[y]
        for x in range(len(line)):
            cur_char = line[x]
            if cur_char == '#':
                matrix_index = (y + padding_all_directions, x + padding_all_directions)
                for cur_dimension in range(additional_dimensions):
                    matrix_index = (padding_all_directions,) + matrix_index
                pocket_dimension[matrix_index] = 1

    return pocket_dimension


def get_index_range(check_index_ranges: list[range]) -> list[tuple]:
    first_range = check_index_ranges[0]
    remaining_ranges = check_index_ranges[1:]
    if any(remaining_ranges):
        indexes_from_remaining_ranges = get_index_range(remaining_ranges)
        return [(item,) + item2 for item in first_range for item2 in indexes_from_remaining_ranges]
    else:
        return [(item,) for item in first_range]


def count_adjacent_cubes(pocket_dimension: np.ndarray, check_indexes: tuple[int]):
    zero_count = 0
    one_count = 0

    # get the ranges of adjacent indexes to check but put a min/max on the ranges to stay within bounds
    shape = pocket_dimension.shape
    check_index_ranges = [range(max(check_index - 1, 0), min(check_index + 2, shape[ind])) for ind, check_index in enumerate(check_indexes)]

    all_cell_coordinates = get_index_range(check_index_ranges)
    for cur_cell_coordinate in all_cell_coordinates:
        # dont check the current cell
        if cur_cell_coordinate == check_indexes:
            continue

        cur_cell_value = pocket_dimension[cur_cell_coordinate]
        if cur_cell_value == 0:
            zero_count += 1
        elif cur_cell_value == 1:
            one_count += 1
        else:
            raise Exception(f'unknown object in array')

    return zero_count, one_count


def perform_cycle(pocket_dimension: np.ndarray):
    # all cell changes happen at once, so
    # perform immutable update on matrix so we don't mess with the current matrix being processed
    shape = pocket_dimension.shape
    future_pocket_dimension = np.zeros(shape, np.int)

    check_index_ranges = [range(0, index_bounds) for ind, index_bounds in enumerate(shape)]
    all_cell_coordinates = get_index_range(check_index_ranges)

    for cur_cell_coordinate in all_cell_coordinates:
        cur_cell_value = future_cell_value = pocket_dimension[cur_cell_coordinate]

        zero_count, one_count = count_adjacent_cubes(pocket_dimension, cur_cell_coordinate)

        # keep the current cell value unless one of these two rules is met
        if cur_cell_value == 1 and (one_count < 2 or one_count > 3):
            future_cell_value = 0
        elif cur_cell_value == 0 and one_count == 3:
            future_cell_value = 1

        future_pocket_dimension[cur_cell_coordinate] = future_cell_value

    return future_pocket_dimension


def run_simulation(file_name: str, num_dimensions: int, num_cycles: int) -> int:
    pocket_dimension = load_pocket_dimension_from_file(file_name, num_dimensions, num_cycles)

    for cur_cycle in range(num_cycles):
        pocket_dimension = perform_cycle(pocket_dimension)

    number_active_cubes = np.count_nonzero(pocket_dimension)
    return number_active_cubes
