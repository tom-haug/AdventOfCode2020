import functools
from abc import ABC, abstractmethod
from copy import deepcopy
from typing import Callable
from day12_navigation_state import NavigationState, Direction


class Instruction(ABC):
    def __init__(self, value: int):
        self.value = value

    @abstractmethod
    def perform(self, nav_state: NavigationState) -> NavigationState:
        pass


#######################
# Part 1 Instructions
#######################
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
        new_nav_state = deepcopy(nav_state)
        num_turns = self.value // 90
        new_nav_state.direction = functools.reduce(lambda prev, cur: prev.rotate(self.clockwise), range(num_turns),
                                                   nav_state.direction)
        return new_nav_state


#######################
# Part 2 Instructions
#######################
class AbsoluteWaypointMoveInstruction(Instruction):
    def __init__(self, direction: Direction, value: int):
        super().__init__(value)
        self.direction = direction

    def perform(self, nav_state: NavigationState) -> NavigationState:
        new_nav_state = nav_state.move_waypoint(self.direction, self.value)
        return new_nav_state


class MoveTowardWaypointInstruction(Instruction):
    def __init__(self, value: int):
        super().__init__(value)

    def perform(self, nav_state: NavigationState) -> NavigationState:
        new_nav_state = deepcopy(nav_state)
        for num_move in range(self.value):
            new_nav_state = new_nav_state.move_toward_waypoint()
        return new_nav_state


class TurnWaypointInstruction(Instruction):
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


def build_instructions_from_file(file_path: str, instruction_factory: Callable[[str], Instruction]):
    f = open(file_path, "r")
    input = f.read().splitlines()
    f.close()
    instructions = [instruction_factory(line) for line in input]
    return instructions


def execute_instructions(initial_nav_state: NavigationState, instructions: list[Instruction]):
    cur_nav_state = deepcopy(initial_nav_state)

    for instruction in instructions:
        cur_nav_state = instruction.perform(cur_nav_state)

    return cur_nav_state
