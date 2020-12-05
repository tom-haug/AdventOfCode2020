import os
import sys
import day03_common


if __name__ == '__main__':
    file_path = os.path.join(sys.path[0], "input.txt")

    total = day03_common.get_tree_count(file_path, 3, 1)
    print('Total', total)
