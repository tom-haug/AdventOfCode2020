import functools
import os
import sys
from abc import ABC, abstractmethod
from copy import deepcopy
from enum import Enum, auto


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def relative_distance_from(self, delta_x, delta_y):
        new_point = Point(self.x + delta_x, self.y + delta_y)
        return new_point

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


class NavigationState:
    def __init__(self, location: Point, direction: Direction, waypoint_offset: Point):
        self.location = location
        self.direction = direction
        self.waypoint_offset = waypoint_offset

    def waypoint_location(self):
        return self.location.relative_distance_from(self.waypoint_offset.x, self.waypoint_offset.y)

    def move_toward_waypoint(self):
        new_nav_state = NavigationState(self.waypoint_location(), self.direction, self.waypoint_offset)
        return new_nav_state

    def move_waypoint(self, direction: Direction, amount: int):
        new_nav_state = deepcopy(self)
        if direction == Direction.North:
            new_nav_state.waypoint_offset.y -= amount
        elif direction == Direction.South:
            new_nav_state.waypoint_offset.y += amount
        elif direction == Direction.West:
            new_nav_state.waypoint_offset.x -= amount
        elif direction == Direction.East:
            new_nav_state.waypoint_offset.x += amount
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
        new_nav_state = nav_state.move_waypoint(self.direction, self.value)
        return new_nav_state


class ForwardMoveInstruction(Instruction):
    def __init__(self, value: int):
        super().__init__(value)

    def perform(self, nav_state: NavigationState) -> NavigationState:
        new_nav_state = deepcopy(nav_state)
        for num_move in range(self.value):
            new_nav_state = new_nav_state.move_toward_waypoint()
        return new_nav_state


class TurnInstruction(Instruction):
    def __init__(self, clockwise: bool, value: int):
        super().__init__(value)
        self.clockwise = clockwise

    def perform(self, nav_state: NavigationState) -> NavigationState:
        new_nav_state = deepcopy(nav_state)
        num_turns = self.value // 90

        for turn in range(num_turns):
            prior_nav_state = deepcopy(new_nav_state)
            if self.clockwise:
                new_nav_state.waypoint_offset.x = prior_nav_state.waypoint_offset.y * -1
                new_nav_state.waypoint_offset.y = prior_nav_state.waypoint_offset.x
            else:
                new_nav_state.waypoint_offset.x = prior_nav_state.waypoint_offset.y
                new_nav_state.waypoint_offset.y = prior_nav_state.waypoint_offset.x * -1

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
    initial_waypoint_offset = Point(10, -1)
    initial_nav_state = NavigationState(Point(0, 0), Direction.East, initial_waypoint_offset)
    cur_nav_state = deepcopy(initial_nav_state)

    for instruction in instructions:
        cur_nav_state = instruction.perform(cur_nav_state)
        print(cur_nav_state.direction)
        print(cur_nav_state.location)

    total_distance = cur_nav_state.location.manhatten_distance_from(initial_nav_state.location)

    print('final location', cur_nav_state.location.x, cur_nav_state.location.y)
    print('total_distance', total_distance)
