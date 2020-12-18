import os
import sys

from day13_common import build_bus_schedules_from_file, get_base_time_for_bus_offsets

if __name__ == '__main__':
    file_path = os.path.join(sys.path[0], "input.txt")
    buses, initial_time = build_bus_schedules_from_file(file_path)
    [print(bus.bus_number, bus.time_offset) for bus in buses]

    base_time = get_base_time_for_bus_offsets(buses)
    print('base_time', base_time)
