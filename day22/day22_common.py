import os.path
import sys
import functools


class CardGame:
    # def __init__(self, file_name: str, recursive_mode: bool):
    #     self.load_input_from_file(file_name)
    #     self.rounds_played = 0
    #     self.recursive_mode = recursive_mode

    def __init__(self, player_one_deck: list[int], player_two_deck: list[int], recursive_mode: bool):
        self.player_one_deck = player_one_deck
        self.player_two_deck = player_two_deck
        self.rounds_played = 0
        self.recursive_mode = recursive_mode
        self.player_one_deck_history: list[str] = []
        self.player_one_override_win = False

        print("Player 1 deck")
        print(player_one_deck)
        print("Player 2 deck")
        print(player_two_deck)

    def play_game(self):
        keep_going = True

        while keep_going:
            keep_going = self.play_round()
            print(f"Round: {self.rounds_played}")

    def play_round(self):
        self.rounds_played += 1

        if self.player_one_deck_serialized() in self.player_one_deck_history:
            self.player_one_override_win = True
            return False

        self.player_one_deck_history.append(self.player_one_deck_serialized())

        player_one_value = self.player_one_deck.pop(0)
        player_two_value = self.player_two_deck.pop(0)

        round_winner = self.determine_round_winner(player_one_value, player_two_value)

        if round_winner == 1:
            self.player_one_deck.append(player_one_value)
            self.player_one_deck.append(player_two_value)
            return len(self.player_two_deck) > 0
        else:
            self.player_two_deck.append(player_two_value)
            self.player_two_deck.append(player_one_value)
            return len(self.player_one_deck) > 0

    def player_one_deck_serialized(self):
        player_one_deck_str_list = [str(val) for val in self.player_one_deck]
        return ",".join(player_one_deck_str_list)

    # def player_one_override_win(self):
    #     return self.player_one_deck_serialized() in self.player_one_deck_history

    def determine_round_winner(self, player_one_value: int, player_two_value: int) -> int:
        if self.recursive_mode and len(self.player_one_deck) >= player_one_value and len(self.player_two_deck) >= player_two_value:
            print("creating sub game")
            sub_game = CardGame(self.player_one_deck[:player_one_value], self.player_two_deck[:player_two_value], self.recursive_mode)
            sub_game.play_game()
            (winning_player_number, winning_score) = sub_game.calculate_winner()
            return winning_player_number
        else:
            return 1 if player_one_value > player_two_value else 2

    def calculate_winner(self) -> (int, int):
        if self.player_one_override_win or len(self.player_two_deck) == 0:
            winning_player_number = 1
            winning_score = self.__calculate_deck_score(self.player_one_deck)
        elif len(self.player_one_deck) == 0:
            winning_player_number = 2
            winning_score = self.__calculate_deck_score(self.player_two_deck)
        else:
            raise Exception("No Winner Yet")

        return (winning_player_number, winning_score)

    def __calculate_deck_score(self, deck: list[int]):
        # card_values = [(len(deck) - idx) * card_value for idx, card_value in enumerate(deck)]
        score = functools.reduce(lambda total, cur: total + ((len(deck) - cur[0]) * cur[1]), enumerate(deck), 0)
        return score


def create_card_game_from_file(file_name: str, recursive_mode: bool) -> CardGame:
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

    card_game = CardGame(player_one_deck, player_two_deck, recursive_mode)
    return card_game