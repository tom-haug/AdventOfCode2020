import os
import sys

from day10_common import load_joltage_list_from_file, get_part01_result_from_joltage_list

if __name__ == '__main__':
    file_path = os.path.join(sys.path[0], "input.txt")
    joltage_list = load_joltage_list_from_file(file_path)

    result = get_part01_result_from_joltage_list(joltage_list)

    print('result', result)
