import functools
import re


class BagRule:
    def __init__(self, bag_name: str, qty: int):
        self.bag_name = bag_name
        self.qty = qty
        self.bag = None


class Bag:
    def __init__(self, input: str):
        self.bag_name = re.match('(.*)\\sbags\\scontain', input)[1]
        contain_bags = re.findall('(\\d+)\\s(.+?)\\sbag', input)
        self.bag_rules = [BagRule(input[1], int(input[0])) for input in contain_bags]

    def can_eventually_contain(self, search_bag):
        found_bag = next((x for x in self.bag_rules if x.bag.bag_name == search_bag), None)
        if found_bag is not None:
            return True
        else:
            for rule in self.bag_rules:
                if rule.bag.can_eventually_contain(search_bag):
                    return True

            return False

    def count_bags_recursive(self) -> int:
        count = 0
        for cur_bag_rule in self.bag_rules:
            count += cur_bag_rule.qty * cur_bag_rule.bag.count_bags_recursive()

        return 1 + count


def build_bags_from_file(file_path):
    f = open(file_path, "r")
    input_lines = f.read().split('\n')
    all_bags = [Bag(line) for line in input_lines]
    f.close()

    for cur_bag in all_bags:
        for bag_rule in cur_bag.bag_rules:
            inner_bag_name = bag_rule.bag_name
            found_inner_bags = [inner_bag for inner_bag in all_bags if inner_bag.bag_name == inner_bag_name]

            if len(found_inner_bags) == 0:
                raise Exception('Inner bag not found')

            bag_rule.bag = found_inner_bags[0]

    return all_bags
