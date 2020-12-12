import os
import sys
from day08_common import Computer, Operation

if __name__ == '__main__':
    file_path = os.path.join(sys.path[0], "input.txt")
    computer = Computer(file_path)
    operation_1 = Operation.NOP
    operation_2 = Operation.JMP
    print('len(computer.instructions)', len(computer.instructions))

    accumulator, ending_instruction_idx, completed_successfully = \
        computer.swap_operations_until_successful(operation_1, operation_2)

    print('accumulator', accumulator)
    print('ending_instruction_idx', ending_instruction_idx)
    print('completed_successfully', completed_successfully)
