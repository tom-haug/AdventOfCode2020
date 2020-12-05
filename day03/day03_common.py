import os
import functools


def build_game_map(input: str):
    lines = input.split("\n")
    game_map = []
    for line in lines:
        line_array = list(line)
        game_map.append(line_array)
    return game_map


def output_game_map(game_map: list):
    os.system('cls')
    for row in game_map:
        cur_line = "".join(row)
        print(cur_line)


def get_object_at_position(game_map: list, x: int, y: int):
    if y > len(game_map):
        return '.'

    reduced_x = x % len(game_map[0])
    cur_object = game_map[y][reduced_x]
    return cur_object


def get_tree_count(file_path: str, slope_x: int, slope_y: int):
    f = open(file_path)
    input = f.read()

    game_map = build_game_map(input)
    output_game_map(game_map)

    y_values = list(range(0, len(game_map), slope_y))
    coordinates = [(idx * slope_x, val) for idx, val in enumerate(y_values)]
    objects = [get_object_at_position(game_map, coord[0], coord[1]) for coord in coordinates]
    tree_count = len([obj for obj in objects if obj == "#"])
    return tree_count


def get_multiplied_tree_counts(file_path: str, slopes: list):
    tree_counts = []
    for slope in slopes:
        tree_counts.append(get_tree_count(file_path, slope[0], slope[1]))

    total = functools.reduce(lambda a, b: a * b, tree_counts)

    return total
