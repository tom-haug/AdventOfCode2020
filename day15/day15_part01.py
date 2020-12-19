
def get_next_number(existing_numbers: list[int]) -> int:
    last_idx = len(existing_numbers) - 1
    last_num = existing_numbers[last_idx]

    try:
        second_last_idx = len(existing_numbers) - existing_numbers[::-1][1:].index(last_num) - 2
    except:
        # this is the first occurrence of the number
        return 0

    # this is the first occurrence of the number
    if second_last_idx == len(existing_numbers) - 1:
        return 0

    return last_idx - second_last_idx


def play_game(initial_state: str, last_turn_num: int):
    spoken_numbers = [int(num_str) for num_str in initial_state.split(',')]

    while len(spoken_numbers) < last_turn_num:
        new_number = get_next_number(spoken_numbers)
        spoken_numbers.append(new_number)

    return spoken_numbers


if __name__ == "__main__":
    input_str = '20,0,1,11,6,3'
    last_turn_num = 2020

    spoken_numbers = play_game(input_str, last_turn_num)

    print('len(spoken_numbers)', len(spoken_numbers))
    print('last_spoken_number:', spoken_numbers[-1])