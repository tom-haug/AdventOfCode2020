from __future__ import annotations
import os
import sys
import re


class InputRule:
    def __init__(self, input_text: str):
        parts = input_text.split(': ')
        id_part = parts[0]
        rules_part = parts[1]

        self.rule_id = int(id_part)
        self.rules_input_str = rules_part  # probably don't need

        first_option_match = re.search(r'^(\d+\s)?(\d+\s)?(\d+)?($|\|)', rules_part)
        if first_option_match is None:
            self.first_option_ordered_rules = {}
        else:
            self.first_option_ordered_rules = [int(group.strip()) for group in first_option_match.groups()[0:-1] if
                                               group]

        second_option_matches = re.search(r'\|\s?(\d+)?\s?(\d+)?\s?(\d+)?$', rules_part)
        if second_option_matches is None:
            self.second_option_ordered_rules = {}
        else:
            self.second_option_ordered_rules = [int(group.strip()) for group in second_option_matches.groups() if group]

        absolute_character_matches = re.search(r'^"(\w+)"$', rules_part)
        if absolute_character_matches is None:
            self.absolute_character_value = None
        else:
            self.absolute_character_value = absolute_character_matches.groups()[0]

    def validate_input_list(self, inputs: list[str], rule_library: dict[int, InputRule]) -> (list[str]):
        return_inputs = []
        for input in inputs:
            return_inputs = return_inputs + self.validate_input(input, rule_library)

        # remove duplicates
        deduped = []
        [deduped.append(x) for x in return_inputs if x not in deduped]
        return deduped

    def validate_input(self, input: str, rule_library: dict[int, InputRule]) -> (list[str]):
        # if we are down to no more input, but there are still rules to satisfy
        # then input is INVALID
        if len(input) == 0:
            return []

        # try absolute character match
        if self.absolute_character_value is not None:
            if input[0] == self.absolute_character_value:
                if len(input) > 1:
                    return [input[1:]]
                else:
                    return ['']
            else:
                return []

        # try first option rules
        remaining_input_first_option = [input]
        # first_option_success = False
        if len(self.first_option_ordered_rules) > 0:
            check_rules = [rule_library[rule] for rule in self.first_option_ordered_rules]
            for cur_rule in check_rules:
                remaining_input_first_option = cur_rule.validate_input_list(remaining_input_first_option, rule_library)
                if len(remaining_input_first_option) == 0:
                    break

        # try second option rules
        remaining_input_second_option = [input]
        # second_option_success = False
        if len(self.second_option_ordered_rules) > 0:
            check_rules = [rule_library[rule] for rule in self.second_option_ordered_rules]
            for cur_rule in check_rules:
                remaining_input_second_option = cur_rule.validate_input_list(remaining_input_second_option, rule_library)
                if len(remaining_input_second_option) == 0:
                    break

        return_inputs = remaining_input_first_option + remaining_input_second_option
        return return_inputs


def load_input_from_file(file_name: str) -> (dict[InputRule], list[str]):
    file_path = os.path.join(sys.path[0], file_name)
    f = open(file_path, "r")
    input_lines = f.read()
    f.close()

    parts = input_lines.split('\n\n')

    rules_section = parts[0]
    message_section = parts[1]

    rules = [InputRule(input_line) for input_line in rules_section.splitlines()]
    rules_dict = {rule.rule_id: rule for rule in rules}

    messages = message_section.splitlines()

    return rules_dict, messages


if __name__ == '__main__':
    file_name = 'input_part02.txt'
    rule_library, messages = load_input_from_file(file_name)
    print('len(rules)', len(rule_library))
    print('messages', messages)

    root_rule = rule_library[0]

    print(root_rule.rule_id)

    message_validation_results = [(message, root_rule.validate_input(message, rule_library)) for message in messages]

    valid_messages = [(message, result) for message, result in message_validation_results if '' in result]

    for message, result in valid_messages:
        print('original message', message)
        print('result', result)
    print(f'valid messages: {len(valid_messages)}')


# part 2: 274 too high
