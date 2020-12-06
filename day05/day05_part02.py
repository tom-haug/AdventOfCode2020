import os
import sys
import math
from day05_common import build_boarding_pass_list_from_file, get_max_seat_boarding_pass, find_missing_seat

if __name__ == '__main__':
    file_path = os.path.join(sys.path[0], "input.txt")
    airplane_rows = 128
    airplane_columns = 8

    boarding_passes = build_boarding_pass_list_from_file(file_path, airplane_rows)

    seat_id = find_missing_seat(boarding_passes, airplane_rows, airplane_columns)

    print('seat_id', seat_id)
