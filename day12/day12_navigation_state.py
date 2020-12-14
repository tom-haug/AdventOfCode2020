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
    def __init__(self, location: Point, direction: Direction, waypoint_offset: Point):
        self.location = location
        self.direction = direction
        self.waypoint_offset = waypoint_offset

    def move(self, direction: Direction, amount: int):
        new_nav_state = deepcopy(self)
        if direction == Direction.North:
            new_nav_state.location.y -= amount
        elif direction == Direction.South:
            new_nav_state.location.y += amount
        elif direction == Direction.West:
            new_nav_state.location.x -= amount
        elif direction == Direction.East:
            new_nav_state.location.x += amount
        return new_nav_state

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
