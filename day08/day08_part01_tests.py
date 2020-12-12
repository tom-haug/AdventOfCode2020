import os
import sys
import unittest

from day08_common import Computer


class TestDay08Part01(unittest.TestCase):

    def test_sample01(self):
        #Arrange
        file_path = os.path.join(sys.path[0], 'input_sample01.txt')
        computer = Computer(file_path)

        # Act
        accumulator, instruction_idx, completed_successfully = computer.execute_loaded_program()

        # Assert
        self.assertEqual(completed_successfully, False)
        self.assertEqual(accumulator, 5)


if __name__ == '__main__':
    unittest.main()