import os
import sys

from day09_common import load_number_list_from_file, find_first_invalid_num

if __name__ == '__main__':
    file_path = os.path.join(sys.path[0], "input.txt")
    num_list = load_number_list_from_file(file_path)
    check_item_count = 25

    first_invalid_num = find_first_invalid_num(num_list, check_item_count)
    print('first_invalid_num', first_invalid_num)
