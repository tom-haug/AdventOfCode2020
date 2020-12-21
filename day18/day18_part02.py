import os
import sys
from enum import Enum
from typing import Optional


class ScrewyEquation:
    def __init__(self, equation_text: str):
        # spaces do nothing for us
        # equation_text = equation_text.strip('(').strip(')')
        equation_text = self.strip_outermost_unnecessary_parans(equation_text)
        equation_text = equation_text.replace(' ', '')

        # we've reached the end, this equation is a static value
        if '+' not in equation_text and '*' not in equation_text:
            self.static_result = int(equation_text)
            return

        # go through equation backwards to maintain left to right precedence
        reversed_equation_text = equation_text[::-1]

        open_paran_count = 0
        first_operand_start = 0
        first_operand_end = - 1
        second_operand_start = -1
        # second_operand_end = len(reversed_equation_text) - 1  # second operand always goes to the end
        current_operator: Optional[str] = None

        while current_operator is None:
            for check_operator in [['*'], ['+']]:
                if current_operator is not None:
                    break

                for idx, value in enumerate(reversed_equation_text):
                    if value == ')':
                        open_paran_count += 1
                    elif value == '(':
                        open_paran_count -= 1
                    elif open_paran_count == 0 and value in check_operator:
                        if first_operand_end == -1:
                            first_operand_end = idx  # - 1
                            second_operand_start = idx + 1
                            current_operator = value
                            break

        second_sub_equation_text = reversed_equation_text[first_operand_start:first_operand_end][::-1]
        first_sub_equation_text = reversed_equation_text[second_operand_start:][::-1]

        self.static_result = None
        self.first_sub_equation = ScrewyEquation(first_sub_equation_text)
        self.second_sub_equation = ScrewyEquation(second_sub_equation_text)
        self.operator = current_operator

    def strip_outermost_unnecessary_parans(self, equation_text: str) -> str:
        # check if parans wrap the entire equation, and remove them
        if equation_text[0] != '(' or equation_text[-1] != ')':
            return equation_text

        open_paran_count = 0
        outermost_wraps_entire_equation = True
        for idx, value in enumerate(equation_text):
            if value == '(':
                open_paran_count += 1
            elif value == ')':
                open_paran_count -= 1
                if open_paran_count == 0 and idx != (len(equation_text) - 1):
                    outermost_wraps_entire_equation = False
                    break

        if not outermost_wraps_entire_equation:
            return equation_text

        return equation_text[1:-1]


    def evaluate(self) -> int:
        if self.static_result is not None:
            return self.static_result
        else:
            first_sub_equation_result = self.first_sub_equation.evaluate()
            second_sub_equation_result = self.second_sub_equation.evaluate()
            if self.operator == '+':
                return first_sub_equation_result + second_sub_equation_result
            elif self.operator == '*':
                return first_sub_equation_result * second_sub_equation_result


def load_equations_from_file(file_name: str) -> list[ScrewyEquation]:
    file_path = os.path.join(sys.path[0], file_name)
    f = open(file_path, "r")
    input_lines = f.read().splitlines()
    f.close()
    equations = [ScrewyEquation(line) for line in input_lines]
    return equations

if __name__ == '__main__':
    file_name = 'input.txt'
    equations = load_equations_from_file(file_name)
    result_sum = 0
    for idx, equation in enumerate(equations):
        result = equations[idx].evaluate()
        result_sum += result
        print(f'Equation {idx} result:', result)
    print('result sum:', result_sum)