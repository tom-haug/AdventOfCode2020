import os
import sys

class Passenger:
    def __init__(self, input: str):
        self.answers = list(input)


class PassengerGroup:
    def __init__(self, input: str):
        passengers_input = input.split('\n')
        self.passengers = [Passenger(passenger) for passenger in passengers_input]

    def get_unique_answers(self):
        all_answers = [answer for passenger in self.passengers for answer in passenger.answers]
        unique_answers = []
        [unique_answers.append(answer) for answer in all_answers if answer not in unique_answers]
        return unique_answers


def build_passengers_from_file(file_path):
    f = open(file_path, "r")
    passenger_group_input = f.read().split('\n\n')
    return [PassengerGroup(group_input) for group_input in passenger_group_input]


if __name__ == '__main__':
    file_path = os.path.join(sys.path[0], "input.txt")

    passenger_groups = build_passengers_from_file(file_path)
    total_unique_answers = [answer for group in passenger_groups for unique_answers in group.get_unique_answers() for answer in unique_answers]
    print('len(total_unique_answers)', len(total_unique_answers))

