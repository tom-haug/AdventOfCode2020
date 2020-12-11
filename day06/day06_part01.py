import os
import sys
from day06_common import build_passengers_from_file


if __name__ == '__main__':
    file_path = os.path.join(sys.path[0], "input.txt")

    passenger_groups = build_passengers_from_file(file_path)
    total_unique_answers = [answer for group in passenger_groups for unique_answers in group.get_unique_answers() for answer in unique_answers]
    print('len(total_unique_answers)', len(total_unique_answers))

