import day22_common as common


def get_part01_result(file_name: str) -> (int, int):
    recursive_mode = False
    card_game = common.create_card_game_from_file(file_name, recursive_mode)
    card_game.play_game()
    return card_game.calculate_winner()


if __name__ == "__main__":
    file_name = "input.txt"
    (winning_player_number, winning_score) = get_part01_result(file_name)

    print("Results")
    print(f"Winner: {winning_player_number}")
    print(f"Score: {winning_score}")