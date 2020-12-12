import os
import sys
from day08_common import Computer


if __name__ == '__main__':
    file_path = os.path.join(sys.path[0], "input.txt")
    computer = Computer(file_path)
    print('len(computer.instructions)', len(computer.instructions))
    accumulator, instruction_idx = computer.execute_loaded_program()
    print('accumulator', accumulator)