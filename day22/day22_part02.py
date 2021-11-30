import day22_common as common

if __name__ == "__main__":
    file_name = "input.txt"
    recursive_mode = True

    card_game = common.create_card_game_from_file(file_name, recursive_mode)

    card_game.play_game()

    (winning_player_number, winning_score) = card_game.calculate_winner()

    print("Results")
    print(f"Total Rounds: {card_game.rounds_played}")
    print("Player 1 deck")
    print(card_game.player_one_deck)
    print("Player 2 deck")
    print(card_game.player_two_deck)
    print(f"Winner: {winning_player_number}")
    print(f"Score: {winning_score}")


# Try one 31300