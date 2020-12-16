import os
import sys


def parse_file(file_path: str):
    f = open(file_path, "r")
    input = f.read().splitlines()
    f.close()
    initial_time = int(input[0])
    buses_input = input[1]
    buses_list = buses_input.split(',')
    buses = [int(bus_input) for bus_input in buses_list if bus_input.isdigit()]

    return initial_time, buses


def next_departure_time(bus_number: int, initial_time: int):
    remainder = initial_time % bus_number
    next_departure = bus_number - remainder
    return next_departure


def get_first_occurange_of_sequence()


if __name__ == '__main__':
    file_path = os.path.join(sys.path[0], "input_sample01.txt")
    initial_time, buses = parse_file(file_path)
    print('buses', buses)

    departure_list = [(bus, next_departure_time(bus, initial_time)) for bus in buses]
    sorted_departure_list = sorted(departure_list, key=lambda item: item[1])
    first_bus_leaving = sorted_departure_list[0];
    print('first_bus_leaving', first_bus_leaving);

    result = first_bus_leaving[0] * first_bus_leaving[1]
    print('result', result)
