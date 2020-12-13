from typing import Callable

import pandas as pd


def build_seat_map_from_file(file_path: str):
    f = open(file_path, "r")
    input = f.read().splitlines()
    f.close()
    jagged_array_input = [list(line) for line in input]
    df = pd.DataFrame(jagged_array_input)
    return df


def step_seat_map(seat_map: pd.DataFrame, adjacent_seat_fn: Callable[[pd.DataFrame, int, int], list[str]], occupied_seat_threshold: int):
    next_seat_map = seat_map.copy()

    for row_idx in range(len(seat_map.index)):
        for col_idx in range(len(seat_map.columns)):
            new_obj = transform_object(seat_map, row_idx, col_idx, adjacent_seat_fn, occupied_seat_threshold)
            next_seat_map.iat[row_idx, col_idx] = new_obj
    return next_seat_map


def transform_object(seat_map: pd.DataFrame, row_idx, col_idx, adjacent_seat_fn: Callable[[pd.DataFrame, int, int], list[str]], occupied_seat_threshold: int):
    cur_obj = seat_map.iat[row_idx, col_idx]

    # empty cells don't need transform
    if cur_obj == '.':
        return '.'

    adjacent_seats = adjacent_seat_fn(seat_map, row_idx, col_idx)

    new_obj = None
    if cur_obj == 'L':
        new_obj = empty_seat_transform(adjacent_seats)
    elif cur_obj == '#':
        new_obj = occupied_seat_transform(adjacent_seats, occupied_seat_threshold)

    if new_obj is None:
        raise Exception('Transformed Object is None')

    return new_obj


def get_adjacent_seats(seat_map: pd.DataFrame, row_idx, col_idx):
    row_count = len(seat_map.index)
    col_count = len(seat_map.columns)
    adjacent_seats = []

    for check_row_idx in range(row_idx - 1, row_idx + 2):
        for check_col_idx in range(col_idx - 1, col_idx + 2):
            if check_row_idx < 0 \
                    or check_row_idx >= row_count \
                    or check_col_idx < 0 \
                    or check_col_idx >= col_count \
                    or (check_row_idx, check_col_idx) == (row_idx, col_idx):
                continue

            adjacent_seats.append(seat_map.iat[check_row_idx, check_col_idx])

    return adjacent_seats


def get_line_of_sight_seats(seat_map: pd.DataFrame, row_idx, col_idx):
    adjacent_seats = []

    for delta_x in range(-1, 2):
        for delta_y in range(-1, 2):
            if (delta_x, delta_y) == (0, 0):
                continue
            first_seat_in_direction = get_first_seat_in_direction(seat_map, row_idx, col_idx, delta_x, delta_y)
            if first_seat_in_direction is not None:
                adjacent_seats.append(first_seat_in_direction)

    return adjacent_seats


def get_first_seat_in_direction(seat_map: pd.DataFrame, row_idx, col_idx, delta_col, delta_row):
    row_count = len(seat_map.index)
    col_count = len(seat_map.columns)
    cur_seat = None
    check_row_idx = row_idx
    check_col_idx = col_idx

    while cur_seat is None or cur_seat == '.':
        check_row_idx += delta_row
        check_col_idx += delta_col
        if check_row_idx < 0 \
                or check_row_idx >= row_count \
                or check_col_idx < 0 \
                or check_col_idx >= col_count \
                or (check_row_idx, check_col_idx) == (row_idx, col_idx):
            break
        cur_seat = seat_map.iat[check_row_idx, check_col_idx]

    return cur_seat


def empty_seat_transform(adjacent_seats):
    occupied_seat_count = len([seat for seat in adjacent_seats if seat == '#'])
    return '#' if occupied_seat_count == 0 else 'L'


def occupied_seat_transform(adjacent_seats: list[str], occupied_seat_threshold: int):
    occupied_seat_count = len([seat for seat in adjacent_seats if seat == '#'])
    return 'L' if occupied_seat_count >= occupied_seat_threshold else '#'


def perform_steps_until_no_change(seat_map, adjacent_seat_fn: Callable[[pd.DataFrame, int, int], list[str]], occupied_seat_threshold: int):
    num_steps = 0
    while True:
        num_steps += 1
        prev_seat_map = seat_map.copy()
        seat_map = step_seat_map(seat_map, adjacent_seat_fn, occupied_seat_threshold)
        if seat_map.equals(prev_seat_map):
            break

    return seat_map, num_steps


def count_cells_with_value(seat_map: pd.DataFrame, search_value: str):
    row_count = len(seat_map.index)
    col_count = len(seat_map.columns)
    count = 0

    for check_row_idx in range(row_count):
        for check_col_idx in range(col_count):
            if seat_map.iat[check_row_idx, check_col_idx] == search_value:
                count += 1
    return count
