import math


def calculate_partitioned_value(partitioning_string: str, lower_partitioning_char: str) -> int:
    cur_lower_bound = 0
    cur_upper_bound = 2 ** len(partitioning_string) - 1
    for char in partitioning_string:
        cur_spread = cur_upper_bound - cur_lower_bound + 1
        half_spread = cur_spread // 2
        if char == lower_partitioning_char:
            cur_upper_bound -= half_spread
        else:
            cur_lower_bound += half_spread

    if cur_upper_bound != cur_lower_bound:
        raise Exception("cur_upper_bound not equal to cur_lower_bound")

    return cur_lower_bound


class BoardingPass:
    def __init__(self, entire_partitioning_string: str, airplane_rows: int):
        self.entire_partitioning_string = entire_partitioning_string

        num_row_chars = int(math.log(airplane_rows) / math.log(2))
        self.row_partitioning_string = entire_partitioning_string[:num_row_chars]
        self.column_partitioning_string = entire_partitioning_string[num_row_chars:]

    def row(self) -> int:
        return calculate_partitioned_value(self.row_partitioning_string, 'F')

    def column(self) -> int:
        return calculate_partitioned_value(self.column_partitioning_string, 'L')

    def seat_id(self) -> int:
        return self.row() * (len(self.row_partitioning_string) + 1) + self.column()


def build_boarding_pass_list_from_file(file_path, airplane_rows: int):
    f = open(file_path, "r")
    input_lines = f.read().splitlines()

    boarding_passes = [BoardingPass(line, airplane_rows) for line in input_lines]
    return boarding_passes


def get_max_seat_boarding_pass(boarding_passes: list[BoardingPass]) -> BoardingPass:
    return max(boarding_passes, key=lambda item: item.seat_id())
