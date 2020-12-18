import numpy as np

class BusSchedule:
    def __init__(self, time_offset: int, bus_number):
        self.time_offset = time_offset
        self.bus_number = bus_number

    def does_bus_arrive_at_offset(self, base_time: int) -> bool:
        result = (base_time + self.time_offset) % self.bus_number
        return result == 0

    def next_departure_time(self, from_time: int = None) -> int:
        if from_time is None:
            from_time = self.time_offset

        remainder = from_time % self.bus_number
        next_departure = self.bus_number - remainder
        return next_departure


def build_bus_schedules_from_file(file_path: str) -> (list[BusSchedule], int):
    f = open(file_path, "r")
    input = f.read().splitlines()
    f.close()
    initial_time = int(input[0])
    buses_input = input[1]
    bus_number_list = [int(bus_input) if bus_input.isdigit() else None for bus_input in buses_input.split(',')]
    bus_schedules = build_bus_schedules_from_bus_number_list(bus_number_list)

    return bus_schedules, initial_time


def build_bus_schedules_from_bus_number_list(bus_number_list: list[int]) -> list[BusSchedule]:
    time_offset = - 1
    bus_schedules: list[BusSchedule] = []
    for bus in bus_number_list:
        time_offset += 1
        if bus is not None:
            bus_schedules.append(BusSchedule(time_offset, bus))
    return bus_schedules


class LinearEquation:
    def __init__(self, m, x, b):
        self.m = m
        self.x = x
        self.b = b

    def get_value(self):
        return self.m * self.x + self.b

    def next(self):
        self.x += 1
        return self.get_value()

    def step_up(self, new_m_components):
        self.b = self.get_value()
        self.x = 0
        int64_m_components = np.array(new_m_components, dtype='int64')
        self.m = np.lcm.reduce(int64_m_components)


def get_base_time_for_bus_offsets(buses: list[BusSchedule]):
    found_busses: list[BusSchedule] = []
    base_time = None

    time_generator = LinearEquation(0, 0, 0)

    for bus in buses:
        while True:
            base_time = time_generator.next()
            if bus.does_bus_arrive_at_offset(base_time):
                break

        found_busses.append(bus)
        time_generator.step_up([bus.bus_number for bus in found_busses])
    return base_time
