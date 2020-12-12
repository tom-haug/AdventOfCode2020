import os
import sys

from day07_common import build_bags_from_file

if __name__ == '__main__':
    file_path = os.path.join(sys.path[0], "input.txt")
    search_bag = 'shiny gold'
    bags = build_bags_from_file(file_path)
    result_bags = [bag for bag in bags if bag.can_eventually_contain(search_bag)]

    [print(bag.bag_name) for bag in result_bags]
    print(len(result_bags))
