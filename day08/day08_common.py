import re
import copy
from enum import Enum


class Operation(Enum):
    NOP = 'nop'
    ACC = 'acc'
    JMP = 'jmp'


class Instruction:
    def __init__(self, input):
        match = re.match('(\\w{3})\\s([+-]\\d+)', input)
        operation_text = match.group(1)
        argument_text = match.group(2)
        self.operation = Operation(operation_text)
        self.argument = int(argument_text)
        self.execution_count = 0

    def reset_execution(self):
        self.execution_count = 0

    def perform_operation(self, input_accumulator, input_instruction_idx):
        self.execution_count += 1

        if self.operation is Operation.NOP:
            return input_accumulator, input_instruction_idx + 1
        elif self.operation is Operation.ACC:
            return input_accumulator + self.argument, input_instruction_idx + 1
        elif self.operation is Operation.JMP:
            return input_accumulator, input_instruction_idx + self.argument


class Computer:
    def __init__(self, file_path):
        self.instructions_template = self.build_instructions_from_file(file_path)
        self.instructions: list[Instruction] = None
        self.reset_instructions()

    @staticmethod
    def build_instructions_from_file(file_path):
        f = open(file_path, "r")
        input_lines = f.read().splitlines()
        instructions = [Instruction(line) for line in input_lines]
        return instructions

    def reset_instructions(self):
        self.instructions = copy.deepcopy(self.instructions_template)

    def swap_instruction_operations(self, instruction_idx: int, from_operation: Operation, to_operation: Operation):
        if self.instructions_template[instruction_idx].operation is from_operation:
            self.instructions[instruction_idx].operation = to_operation

    def execute_loaded_program(self):
        instruction_idx = 0
        accumulator = 0
        completed_successfully = False

        [instruction.reset_execution() for instruction in self.instructions]
        cur_instruction = self.instructions[instruction_idx]

        while cur_instruction.execution_count == 0:
            accumulator, instruction_idx = cur_instruction.perform_operation(accumulator, instruction_idx)

            if instruction_idx == len(self.instructions):
                completed_successfully = True
                break
            elif instruction_idx > len(self.instructions):
                break

            cur_instruction = self.instructions[instruction_idx]

        return accumulator, instruction_idx, completed_successfully

    def swap_operations_until_successful(self, operation_1, operation_2):
        for try_modify_instruction_idx in range(len(self.instructions_template)):
            self.reset_instructions()
            self.swap_instruction_operations(try_modify_instruction_idx, Operation.NOP, Operation.JMP)
            self.swap_instruction_operations(try_modify_instruction_idx, Operation.JMP, Operation.NOP)

            accumulator, ending_instruction_idx, completed_successfully = self.execute_loaded_program()

            if completed_successfully:
                return accumulator, ending_instruction_idx, completed_successfully
