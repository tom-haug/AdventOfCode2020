def update_spoken_numbers(spoken_numbers:dict[int, int], new_number: int, turn_num: int):
    spoken_numbers[new_number] = turn_num


def play_game(initial_state: str, last_turn_num: int):
    initial_numbers = [int(num_str) for num_str in initial_state.split(',')]
    spoken_numbers = {}

    turn_num = 0
    last_num_spoken = None
    for turn_num in range(1, len(initial_numbers) + 1):
        last_num_spoken = initial_numbers[turn_num - 1]
        update_spoken_numbers(spoken_numbers, last_num_spoken, turn_num)

    previous_turn_last_number_was_spoken = spoken_numbers[last_num_spoken]
    while turn_num < last_turn_num:
        last_num_spoken = turn_num - previous_turn_last_number_was_spoken
        turn_num += 1

        if last_num_spoken in spoken_numbers.keys():
            previous_turn_last_number_was_spoken = spoken_numbers[last_num_spoken]
        else:
            previous_turn_last_number_was_spoken = turn_num

        update_spoken_numbers(spoken_numbers, last_num_spoken, turn_num)

    return last_num_spoken