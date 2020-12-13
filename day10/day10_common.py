from itertools import permutations

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


def get_valid_combinations_single_adapter(sorted_joltage_dict: dict[int, int], cur_adapter_key: int):
    valid_next_adapter_keys = [cur_key for cur_key in sorted_joltage_dict.keys() if cur_adapter_key < cur_key <= (cur_adapter_key + 3)]

    # this is the very last adapter, there is one possibility
    if len(valid_next_adapter_keys) == 0:
        subsequent_combinations = 1
    else:
        subsequent_combinations = sum([sorted_joltage_dict[adapter_key] for adapter_key in valid_next_adapter_keys])

    return subsequent_combinations


def get_all_valid_adapter_combinations(joltage_list: dict[int, int]):
    sorted_joltage_list = sorted(joltage_list)
    sorted_joltage_dict = {i: 0 for i in sorted_joltage_list}

    for joltage in reversed(sorted_joltage_list):
        valid_adapter_combinations = get_valid_combinations_single_adapter(sorted_joltage_dict, joltage)
        sorted_joltage_dict[joltage] = valid_adapter_combinations

    total_combinations = sorted_joltage_dict[sorted_joltage_list[0]]
    return total_combinations
