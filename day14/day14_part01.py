from day14_common import process_instructions_from_file, MemoryBank

if __name__ == '__main__':
    file_path = 'input.txt'
    memory_bank = MemoryBank(36)
    process_instructions_from_file(file_path, memory_bank.set_value_mask, memory_bank.set_memory_value)
    result = memory_bank.memory_address_sum()
    print('result', result)
