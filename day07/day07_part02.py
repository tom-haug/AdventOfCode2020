import os
import sys

from day07_common import build_bags_from_file

if __name__ == '__main__':
    file_path = os.path.join(sys.path[0], "input.txt")
    search_bag = 'shiny gold'
    bags = build_bags_from_file(file_path)

    shiney_gold_bag = next((bag for bag in bags if bag.bag_name == search_bag), None)

    total_count = shiney_gold_bag.count_bags_recursive() - 1

    print('total_count', total_count)
