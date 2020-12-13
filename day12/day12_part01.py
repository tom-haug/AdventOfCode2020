import functools
import os
import sys
from abc import ABC, abstractmethod
from copy import copy
from enum import Enum, auto


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def manhatten_distance_from(self, other_point):
        if not isinstance(other_point, Point):
            raise Exception('Manhatten distance can only ben generated from two Points')

        delta_x = abs(self.x - other_point.x)
        delta_y = abs(self.y - other_point.y)
        manhatten_distance = delta_x + delta_y
        return manhatten_distance


class Direction(Enum):
    North = auto()
    South = auto()
    East = auto()
    West = auto()

    def rotate(self, clockwise: bool):
        if self is Direction.North:
            return Direction.East if clockwise else Direction.West
        elif self is Direction.East:
            return Direction.South if clockwise else Direction.North
        elif self is Direction.South:
            return Direction.West if clockwise else Direction.East
        elif self is Direction.West:
            return Direction.North if clockwise else Direction.South
        else:
            raise Exception("Unknown Enum direction")

class NavigationState:
    def __init__(self, location: Point, direction: Direction):
        self.location = location
        self.direction = direction

    def move(self, direction: Direction, amount: int):
        new_nav_state = copy(self)
        if direction == Direction.North:
            new_nav_state.location.y -= amount
        elif direction == Direction.South:
            new_nav_state.location.y += amount
        elif direction == Direction.West:
            new_nav_state.location.x -= amount
        elif direction == Direction.East:
            new_nav_state.location.x += amount
        return new_nav_state


class Instruction(ABC):
    def __init__(self, value: int):
        self.value = value

    @abstractmethod
    def perform(self, nav_state: NavigationState) -> NavigationState:
        pass


class AbsoluteMoveInstruction(Instruction):
    def __init__(self, direction: Direction, value: int):
        super().__init__(value)
        self.direction = direction

    def perform(self, nav_state: NavigationState) -> NavigationState:
        new_nav_state = nav_state.move(self.direction, self.value)
        return new_nav_state


class ForwardMoveInstruction(Instruction):
    def __init__(self, value: int):
        super().__init__(value)

    def perform(self, nav_state: NavigationState) -> NavigationState:
        new_nav_state = nav_state.move(nav_state.direction, self.value)
        return new_nav_state


class TurnInstruction(Instruction):
    def __init__(self, clockwise: bool, value: int):
        super().__init__(value)
        self.clockwise = clockwise

    def perform(self, nav_state: NavigationState) -> NavigationState:
        new_nav_state = copy(nav_state)
        num_turns = self.value // 90
        new_nav_state.direction = functools.reduce(lambda prev, cur: prev.rotate(self.clockwise) , range(num_turns), nav_state.direction)
        return new_nav_state


def instruction_factory(input: str) -> Instruction:
    type = input[0]
    value = int(input[1:])
    if type == 'N':
        return AbsoluteMoveInstruction(Direction.North, value)
    elif type == 'S':
        return AbsoluteMoveInstruction(Direction.South, value)
    elif type == 'E':
        return AbsoluteMoveInstruction(Direction.East, value)
    elif type == 'W':
        return AbsoluteMoveInstruction(Direction.West, value)
    elif type == 'F':
        return ForwardMoveInstruction(value)
    elif type == 'L':
        return TurnInstruction(False, value)
    elif type == 'R':
        return TurnInstruction(True, value)


def build_instructions_from_file(file_path):
    f = open(file_path, "r")
    input = f.read().splitlines()
    f.close()
    instructions = [instruction_factory(line) for line in input]
    return instructions


if __name__ == '__main__':
    file_path = os.path.join(sys.path[0], "input.txt")
    instructions = build_instructions_from_file(file_path)
    initial_nav_state = NavigationState(Point(0, 0), Direction.East)
    cur_nav_state = NavigationState(Point(0, 0), Direction.East)

    for instruction in instructions:
        cur_nav_state = instruction.perform(cur_nav_state)
        print(cur_nav_state.direction)
        print(cur_nav_state.location)

    total_distance = cur_nav_state.location.manhatten_distance_from(initial_nav_state.location)

    print('total_distance', total_distance)

