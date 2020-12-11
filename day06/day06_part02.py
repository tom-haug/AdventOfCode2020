import os
import sys
from day06_common import build_passengers_from_file


if __name__ == '__main__':
    file_path = os.path.join(sys.path[0], "input.txt")

    passenger_groups = build_passengers_from_file(file_path)
    total_common_answers = [answer for group in passenger_groups for common_answers in group.get_common_answers() for answer in common_answers]
    print('len(total_common_answers)', len(total_common_answers))

