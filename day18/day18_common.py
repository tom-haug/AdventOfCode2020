import os
import sys
from typing import Optional


class ScrewyEquation:
    def __init__(self, equation_text: str, operator_precedence: list[list[str]]):
        self.static_result: Optional[int] = None

        # get rid of parens that wrap the whole equation
        equation_text = self.strip_outermost_unnecessary_parens(equation_text)
        # spaces do nothing for us
        equation_text = equation_text.replace(' ', '')

        # we've reached the end, this equation evaluates to a static value
        if '+' not in equation_text and '*' not in equation_text:
            self.static_result = int(equation_text)
            return

        # process equation backwards to maintain left to right precedence
        equation_text = equation_text[::-1]

        open_paren_count = 0
        first_operand_start = 0
        first_operand_end = - 1
        second_operand_start = -1
        selected_operator: Optional[str] = None

        for check_operator in operator_precedence:
            # if we have already found the operator to use, don't keep checking
            if selected_operator is not None:
                break

            for idx, value in enumerate(equation_text):
                # since we are going backwards through the equation, the open/close parens will look backwards
                if value == ')':
                    open_paren_count += 1
                elif value == '(':
                    open_paren_count -= 1
                elif open_paren_count == 0 and value in check_operator:
                    # we have found the break between the two operands!
                    first_operand_end = idx
                    second_operand_start = idx + 1
                    selected_operator = value
                    break

        # split apart this equation based on the split point determined above
        # reverse these again so they are the back to normal when we pass them into the next ScrewyEquation
        second_sub_equation_text = equation_text[first_operand_start:first_operand_end][::-1]
        first_sub_equation_text = equation_text[second_operand_start:][::-1]

        self.first_sub_equation = ScrewyEquation(first_sub_equation_text, operator_precedence)
        self.second_sub_equation = ScrewyEquation(second_sub_equation_text, operator_precedence)
        self.operator = selected_operator

    @staticmethod
    def strip_outermost_unnecessary_parens(equation_text: str) -> str:
        # if parens don't wrap the whole equation, we don't need to do anything
        if equation_text[0] != '(' or equation_text[-1] != ')':
            return equation_text

        open_paren_count = 0
        outermost_wraps_entire_equation = True
        for idx, value in enumerate(equation_text):
            if value == '(':
                open_paren_count += 1
            elif value == ')':
                open_paren_count -= 1
                # if we are at the root of the equation and we found a matching ending paren part-way through
                if open_paren_count == 0 and idx != (len(equation_text) - 1):
                    outermost_wraps_entire_equation = False
                    break

        # parens exist around entire equation, but they are not matching, so do not alter the equation
        if not outermost_wraps_entire_equation:
            return equation_text

        # slice the equation, removing first and last characters
        return equation_text[1:-1]

    def evaluate(self) -> int:
        # return either the static value or recurse through the child equations
        # and perform the current operator on the results
        if self.static_result is not None:
            return self.static_result
        else:
            first_sub_equation_result = self.first_sub_equation.evaluate()
            second_sub_equation_result = self.second_sub_equation.evaluate()
            if self.operator == '+':
                return first_sub_equation_result + second_sub_equation_result
            elif self.operator == '*':
                return first_sub_equation_result * second_sub_equation_result


def load_equations_from_file(file_name: str, operator_precedence: list[list[str]]) -> list[ScrewyEquation]:
    file_path = os.path.join(sys.path[0], file_name)
    f = open(file_path, "r")
    input_lines = f.read().splitlines()
    f.close()
    equations = [ScrewyEquation(line, operator_precedence) for line in input_lines]
    return equations