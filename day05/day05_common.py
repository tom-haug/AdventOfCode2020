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


def calculate_seat_id(row: int, column: int, row_multiplier: int):
    return row * row_multiplier + column


class BoardingPass:
    def __init__(self, entire_partitioning_string: str, airplane_rows: int):
        self.entire_partitioning_string = entire_partitioning_string

        num_row_chars = int(math.log(airplane_rows) / math.log(2))
        self.row_partitioning_string = entire_partitioning_string[:num_row_chars]
        self.column_partitioning_string = entire_partitioning_string[num_row_chars:]
        self.row = calculate_partitioned_value(self.row_partitioning_string, 'F')
        self.column = calculate_partitioned_value(self.column_partitioning_string, 'L')

    def seat_id(self) -> int:
        return calculate_seat_id(self.row, self.column, len(self.row_partitioning_string) + 1)


def build_boarding_pass_list_from_file(file_path, airplane_rows: int):
    f = open(file_path, "r")
    input_lines = f.read().splitlines()

    boarding_passes = [BoardingPass(line, airplane_rows) for line in input_lines]
    return boarding_passes


def get_max_seat_boarding_pass(boarding_passes: list[BoardingPass]) -> BoardingPass:
    return max(boarding_passes, key=lambda item: item.seat_id())


def find_missing_seat(boarding_passes: list[BoardingPass], airplane_rows: int, airplane_columns) -> int:
    row_multiplier = int(math.log(airplane_rows) / math.log(2)) + 1

    for row in range(airplane_rows):
        for col in range(airplane_columns):
            boarding_pass = next((x for x in boarding_passes if x.row == row and x.column == col), None)
            if boarding_pass is None:
                seat_id = calculate_seat_id(row, col, row_multiplier)

                # make sure previous and next seat exist
                prior_boarding_pass = next((x for x in boarding_passes if x.seat_id() == seat_id - 1), None)
                next_boarding_pass = next((x for x in boarding_passes if x.seat_id() == seat_id + 1), None)

                if prior_boarding_pass is not None and next_boarding_pass is not None:
                    return seat_id

    raise Exception('missing seat not found')
