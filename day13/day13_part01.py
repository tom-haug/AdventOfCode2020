import os
import sys
from day13_common import build_bus_schedules_from_file


def get_part01_result_from_file(file_path: str) -> int:
    buses, initial_time = build_bus_schedules_from_file(file_path)

    departure_list = [bus for bus in buses]
    sorted_departure_list = sorted(departure_list, key=lambda item: item.next_departure_time(initial_time))

    first_bus_leaving = sorted_departure_list[0];

    result = first_bus_leaving.bus_number * first_bus_leaving.next_departure_time(initial_time)
    return result


if __name__ == '__main__':
    file_path = os.path.join(sys.path[0], "input.txt")

    result = get_part01_result_from_file(file_path)

    print('result', result)
