import os
import sys
import math
from day05_common import build_boarding_pass_list_from_file, get_max_seat_boarding_pass

if __name__ == '__main__':
    file_path = os.path.join(sys.path[0], "input.txt")
    airplane_rows = 128

    boarding_passes = build_boarding_pass_list_from_file(file_path, airplane_rows)
    max_seat_boarding_pass = get_max_seat_boarding_pass(boarding_passes)

    print('seat_id', max_seat_boarding_pass.seat_id())

