import os
import sys


def load_joltage_list_from_file(file_path) -> list[int]:
    f = open(file_path, "r")
    input_lines = f.read().splitlines()
    nums = [int(line) for line in input_lines]
    f.close()
    return nums


def get_joltage_delta_list_from_joltage_list(joltage_list):
    sorted_joltage_list = sorted(joltage_list)
    joltage_delta_list: list[int] = []

    for cur_idx in range(len(sorted_joltage_list)):
        cur_joltage = sorted_joltage_list[cur_idx]
        prev_joltage = sorted_joltage_list[cur_idx - 1] if cur_idx > 0 else 0
        joltage_delta = cur_joltage - prev_joltage
        joltage_delta_list.append(joltage_delta)

    joltage_delta_list.append(3)  # device joltage is always 3 more than max adapter

    return joltage_delta_list


def get_part01_result_from_joltage_delta_list(joltage_delta_list):
    one_joltage_difference = [joltage_delta for joltage_delta in joltage_delta_list if joltage_delta == 1]
    three_joltage_difference = [joltage_delta for joltage_delta in joltage_delta_list if joltage_delta == 3]

    one_joltage_difference_count = len(one_joltage_difference)
    three_joltage_difference_count = len(three_joltage_difference)

    result = one_joltage_difference_count * three_joltage_difference_count
    return result


def get_part01_result_from_joltage_list(joltage_list):
    joltage_delta_list = get_joltage_delta_list_from_joltage_list(joltage_list)
    result = get_part01_result_from_joltage_delta_list(joltage_delta_list)
    return result


if __name__ == '__main__':
    file_path = os.path.join(sys.path[0], "input.txt")
    joltage_list = load_joltage_list_from_file(file_path)

    result = get_part01_result_from_joltage_list(joltage_list)

    print('result', result)
