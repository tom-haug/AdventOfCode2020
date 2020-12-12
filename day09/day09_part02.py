import os
import sys

from day09_common import load_number_list_from_file, find_encryption_weakness_from_initial_input

if __name__ == '__main__':
    file_path = os.path.join(sys.path[0], "input.txt")
    num_list = load_number_list_from_file(file_path)
    check_item_count = 25

    encryption_weakness = find_encryption_weakness_from_initial_input(num_list, check_item_count)
    print('encryption_weakness', encryption_weakness)
