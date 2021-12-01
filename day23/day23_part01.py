import os
import sys

sys.path.append("..")
from shared.doubly_linked_node import DoublyLinkedNode


class CupGame:
    def __init__(self, file_name: str):
        self.current_cup = self.load_cups_from_file(file_name)

    def load_cups_from_file(self, file_name: str) -> DoublyLinkedNode[int]:
        file_path = os.path.join(sys.path[0], file_name)
        f = open(file_path, "r")
        file_contents = f.read()
        f.close()

        cups = [DoublyLinkedNode[int](int(char)) for char in file_contents]
        first_cup = cups[0]
        for cur_cup in cups[:0:-1]:
            first_cup.append(cur_cup)
        return first_cup

    def move(self):
        remove_cup_1 = self.current_cup.next.remove_self()
        remove_cup_2 = self.current_cup.next.remove_self()
        remove_cup_3 = self.current_cup.next.remove_self()

        destination_cup_label = self.current_cup.data - 1
        while destination_cup_label in [remove_cup_1.data, remove_cup_2.data,  remove_cup_3.data]:
            destination_cup_label -= 1

        if destination_cup_label < self.current_cup.min_connected_node().data:
            destination_cup_label = self.current_cup.max_connected_node().data

        destination_cup = self.current_cup.get_connected_node(destination_cup_label)
        destination_cup.append(remove_cup_3)
        destination_cup.append(remove_cup_2)
        destination_cup.append(remove_cup_1)
        self.current_cup = self.current_cup.next

    def get_cup_order(self) -> str:
        cup_one = self.current_cup.get_connected_node(1)
        cup_order = ""
        cur_cup = cup_one.next
        while cur_cup != cup_one:
            cup_order += str(cur_cup.data)
            cur_cup = cur_cup.next
        return cup_order


def get_part01_result(file_name: str) -> str:
    cup_game = CupGame(file_name)
    for _ in range(100):
        cup_game.move()

    cup_order = cup_game.get_cup_order()
    print(cup_order)


if __name__ == "__main__":
    file_name = "input.txt"
    result = get_part01_result(file_name)
    print(f"Result: {result}")
