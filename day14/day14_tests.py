import unittest

from day14_common import MemoryBank, process_instructions_from_file


class TestDay14(unittest.TestCase):
    def test_part01(self):
        # Arrange
        file_path = 'input_sample01.txt'
        memory_bank = MemoryBank(36)

        # Act
        process_instructions_from_file(file_path, memory_bank.set_value_mask, memory_bank.set_memory_value)
        result = memory_bank.memory_address_sum()

        # Assert
        self.assertEqual(result, 165)

    def test_part02(self):
        # Arrange
        file_path = 'input_sample02.txt'
        memory_bank = MemoryBank(36)

        # Act
        process_instructions_from_file(file_path, memory_bank.set_address_mask, memory_bank.set_memory_value)
        result = memory_bank.memory_address_sum()

        # Assert
        self.assertEqual(result, 208)


if __name__ == '__main__':
    unittest.main()
