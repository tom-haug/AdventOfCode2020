import os.path
import sys
import functools


class CardGame:
    def __init__(self, file_name: str):
        self.load_input_from_file(file_name)
        self.rounds_played = 0

    def load_input_from_file(self, file_name: str):
        file_path = os.path.join(sys.path[0], file_name)
        f = open(file_path, "r")
        file_contents = f.read()
        f.close()

        player_one_deck: list[int] = []
        player_two_deck: list[int] = []
        cur_deck: list[int] = None
        for cur_line in file_contents.splitlines():
            cur_line = cur_line.strip()
            if cur_line == "Player 1:":
                cur_deck = player_one_deck
            elif cur_line == "Player 2:":
                cur_deck = player_two_deck
            elif len(cur_line) > 0:
                cur_deck.append(int(cur_line))

        self.player_one_deck = player_one_deck
        self.player_two_deck = player_two_deck

    def play_round(self):
        self.rounds_played += 1
        player_one_value = self.player_one_deck.pop(0)
        player_two_value = self.player_two_deck.pop(0)
        if player_one_value > player_two_value:
            self.player_one_deck.append(player_one_value)
            self.player_one_deck.append(player_two_value)
            return len(self.player_two_deck) > 0
        else:
            self.player_two_deck.append(player_two_value)
            self.player_two_deck.append(player_one_value)
            return len(self.player_one_deck) > 0

    def calculate_winner(self) -> (int, int):
        winning_player_number: int = None
        winning_score: int = None
        if len(self.player_one_deck) == 0:
            winning_player_number = 2
            winning_score = self.__calculate_deck_score(self.player_two_deck)
        elif len(self.player_two_deck) == 0:
            winning_player_number = 1
            winning_score = self.__calculate_deck_score(self.player_one_deck)
        else:
            raise Exception("No Winner Yet")

        return (winning_player_number, winning_score)

    def __calculate_deck_score(self, deck: list[int]):
        # card_values = [(len(deck) - idx) * card_value for idx, card_value in enumerate(deck)]
        score = functools.reduce(lambda total, cur: total + ((len(deck) - cur[0]) * cur[1]), enumerate(deck), 0)
        return score


if __name__ == "__main__":
    file_name = "input.txt"
    card_game = CardGame(file_name)

    print("Initial Decks")
    print("Player 1 deck")
    print(card_game.player_one_deck)
    print("Player 2 deck")
    print(card_game.player_two_deck)

    keep_going = True

    while keep_going:
        keep_going = card_game.play_round()
        print(f"Round: {card_game.rounds_played}")

    (winning_player_number, winning_score) = card_game.calculate_winner()

    print("Results")
    print(f"Total Rounds: {card_game.rounds_played}")
    print("Player 1 deck")
    print(card_game.player_one_deck)
    print("Player 2 deck")
    print(card_game.player_two_deck)
    print(f"Winner: {winning_player_number}")
    print(f"Score: {winning_score}")