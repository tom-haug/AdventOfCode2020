import os
import sys
import day04_common


if __name__ == '__main__':
    file_path = os.path.join(sys.path[0], "input.txt")
    rules = day04_common.basic_password_rules()

    count = day04_common.get_valid_passport_count(file_path, rules)
    print('Valid Passports', count)
