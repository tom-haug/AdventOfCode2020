import os
import sys
from day12_navigation_state import NavigationState, Point, Direction
from day12_instruction_library import build_instructions_from_file, execute_instructions, AbsoluteMoveInstruction, ForwardMoveInstruction, TurnInstruction, \
    Instruction


def part01_instruction_factory(input: str) -> Instruction:
    instruction_type = input[0]
    value = int(input[1:])

    if instruction_type == 'N':
        return AbsoluteMoveInstruction(Direction.North, value)
    elif instruction_type == 'S':
        return AbsoluteMoveInstruction(Direction.South, value)
    elif instruction_type == 'E':
        return AbsoluteMoveInstruction(Direction.East, value)
    elif instruction_type == 'W':
        return AbsoluteMoveInstruction(Direction.West, value)
    elif instruction_type == 'F':
        return ForwardMoveInstruction(value)
    elif instruction_type == 'L':
        return TurnInstruction(False, value)
    elif instruction_type == 'R':
        return TurnInstruction(True, value)


if __name__ == '__main__':
    file_path = os.path.join(sys.path[0], "input.txt")
    instructions = build_instructions_from_file(file_path, part01_instruction_factory)
    initial_nav_state = NavigationState(Point(0, 0), Direction.East, None)

    final_nav_state = execute_instructions(initial_nav_state, instructions)

    total_distance = final_nav_state.location.manhatten_distance_from(initial_nav_state.location)

    print('total_distance', total_distance)

