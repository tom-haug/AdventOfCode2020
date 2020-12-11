import pandas as pd

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

    def get_common_answers(self):
        # get all answers for all passengers
        all_answers = [answer for passenger in self.passengers for answer in passenger.answers]
        df = pd.DataFrame({'answer': all_answers})

        # get count of each answer
        grouped_df = df.groupby(['answer'])['answer'].count().reset_index(name="count")

        # filter on answers that all passengers have answered
        filtered_df = grouped_df[grouped_df['count'] == len(self.passengers)]

        common_answers = filtered_df['answer'].values.tolist()
        return common_answers



def build_passengers_from_file(file_path):
    f = open(file_path, "r")
    passenger_group_input = f.read().split('\n\n')
    return [PassengerGroup(group_input) for group_input in passenger_group_input]
