import os
import sys
from day12_navigation_state import Point, NavigationState, Direction
from day12_instruction_library import build_instructions_from_file, AbsoluteWaypointMoveInstruction, MoveTowardWaypointInstruction, \
    TurnWaypointInstruction, Instruction, execute_instructions


def part02_instruction_factory(input: str) -> Instruction:
    instruction_type = input[0]
    value = int(input[1:])

    if instruction_type == 'N':
        return AbsoluteWaypointMoveInstruction(Direction.North, value)
    elif instruction_type == 'S':
        return AbsoluteWaypointMoveInstruction(Direction.South, value)
    elif instruction_type == 'E':
        return AbsoluteWaypointMoveInstruction(Direction.East, value)
    elif instruction_type == 'W':
        return AbsoluteWaypointMoveInstruction(Direction.West, value)
    elif instruction_type == 'F':
        return MoveTowardWaypointInstruction(value)
    elif instruction_type == 'L':
        return TurnWaypointInstruction(False, value)
    elif instruction_type == 'R':
        return TurnWaypointInstruction(True, value)


if __name__ == '__main__':
    file_path = os.path.join(sys.path[0], "input.txt")
    initial_waypoint_offset = Point(10, -1)
    instructions = build_instructions_from_file(file_path, part02_instruction_factory)
    initial_nav_state = NavigationState(Point(0, 0), Direction.East, initial_waypoint_offset)

    final_nav_state = execute_instructions(initial_nav_state, instructions)

    total_distance = final_nav_state.location.manhatten_distance_from(initial_nav_state.location)

    print('final location', final_nav_state.location.x, final_nav_state.location.y)
    print('total_distance', total_distance)
