import os
import sys
from day03 import day03_common


if __name__ == '__main__':
    file_path = os.path.join(sys.path[0], "input.txt")
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

    total = day03_common.get_multiplied_tree_counts(file_path, slopes)
    print('Total', total)
