import os
import sys
import unittest

from day08_common import Computer, Operation


class TestDay08Part01(unittest.TestCase):

    def test_sample01(self):
        #Arrange
        file_path = os.path.join(sys.path[0], 'input_sample01.txt')
        computer = Computer(file_path)
        operation_1 = Operation.NOP
        operation_2 = Operation.JMP

        # Act
        accumulator, ending_instruction_idx, completed_successfully = \
            computer.swap_operations_until_successful(operation_1, operation_2)

        # Assert
        self.assertEqual(completed_successfully, True)
        self.assertEqual(accumulator, 8)


if __name__ == '__main__':
    unittest.main()