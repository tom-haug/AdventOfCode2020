import os
import sys

from day10_common import load_joltage_list_from_file, get_all_valid_adapter_combinations

if __name__ == '__main__':
    file_path = os.path.join(sys.path[0], "input.txt")
    joltage_list = load_joltage_list_from_file(file_path)
    joltage_list.append(0) # add the wall as a node

    total_combinations = get_all_valid_adapter_combinations(joltage_list)

    print('total_combinations', total_combinations)
