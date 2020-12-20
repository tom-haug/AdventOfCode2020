import os
import sys
import numpy as np
np.set_printoptions(threshold=sys.maxsize)


def load_pocket_dimension_from_file(file_name: str, padding_all_directions: int):
    file_path = os.path.join(sys.path[0], file_name)
    f = open(file_path, "r")
    input_lines = f.read().splitlines()
    f.close()

    initial_height = len(input_lines)
    initial_width = len(input_lines[0])
    initial_depth = 1

    offset_x = offset_y = offset_z = padding_all_directions

    padded_initial_height = initial_height + 2 * padding_all_directions
    padded_initial_width = initial_width + 2 * padding_all_directions
    padded_initial_depth = initial_depth + 2 * padding_all_directions

    pocket_dimension = np.zeros((padded_initial_depth, padded_initial_height, padded_initial_width), np.int)

    # print(pocket_dimension)

    for y in range(len(input_lines)):
        line = input_lines[y]
        for x in range(len(line)):
            cur_char = line[x]
            if cur_char == '#':
                pocket_dimension[padding_all_directions, y + padding_all_directions, x + padding_all_directions] = 1

    return pocket_dimension


def count_adjacent_cubes(pocket_dimension: np.ndarray, z: int, y: int, x: int):
    zero_count = 0
    one_count = 0
    z_length, y_length, x_length = pocket_dimension.shape

    for cur_z in range(z - 1, z + 2):
        if cur_z < 0 or cur_z >= z_length:
            continue
        for cur_y in range(y - 1, y + 2):
            if cur_y < 0 or cur_y >= y_length:
                continue
            for cur_x in range(x - 1, x + 2):
                if cur_x < 0 or cur_x >= x_length:
                    continue
                if (cur_z, cur_y, cur_x) == (z, y, x):
                    continue

                cur_object = pocket_dimension[cur_z, cur_y, cur_x]
                if cur_object == 0:
                    zero_count += 1
                elif cur_object == 1:
                    one_count += 1
                else:
                    raise Exception(f'unknown object at {z}, {y}, {x}: {cur_object}')
    return zero_count, one_count


def perform_cycle(pocket_dimension: np.ndarray):
    z_length, y_length, x_length = pocket_dimension.shape
    future_pocket_dimension = np.zeros((z_length, y_length, x_length), np.int)

    for z in range(z_length):
        for y in range(y_length):
            for x in range(x_length):
                current_state = future_state = pocket_dimension[z, y, x]
                zero_count, one_count = count_adjacent_cubes(pocket_dimension, z, y, x)
                if current_state == 1 and (one_count < 2 or one_count > 3):
                    future_state = 0
                elif current_state == 0 and one_count == 3:
                    future_state = 1

                future_pocket_dimension[z, y, x] = future_state
    return future_pocket_dimension


if __name__ == "__main__":
    file_name = 'input.txt'
    pocket_dimension = load_pocket_dimension_from_file(file_name, 6)

    print('initial')
    print(pocket_dimension)
    for cur_cycle in range(6):

        pocket_dimension = perform_cycle(pocket_dimension)

        os.system('cls')
        print('cur_cycle', cur_cycle)
        print(pocket_dimension)
        print('nonzero', np.count_nonzero(pocket_dimension))