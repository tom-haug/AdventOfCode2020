import os
import sys
import re


def build_password_list(lines):
    regex = re.compile("(\d+)-(\d+)\s(\w):\s(\w+)")
    passwords = []
    for line in lines:
        match = regex.match(line)
        pos1, pos2, expected_char, password = match.group(1, 2, 3, 4)
        passwords.append((int(pos1), int(pos2), expected_char, password))
    return passwords


def get_valid_passwords(passwords):
    return [password for password in passwords if (password[3][password[0] - 1] == password[2]) != (password[3][password[1] - 1] == password[2])]


def get_valid_password_count(file_path):
    f = open(file_path, "r")
    input_str = f.read()
    lines = input_str.split("\n")

    passwords = build_password_list(lines)

    valid_passwords = get_valid_passwords(passwords)

    return len(valid_passwords)


if __name__ == '__main__':
    filePath = os.path.join(sys.path[0], "input.txt")
    count = get_valid_password_count(filePath)
    print('Valid Password Count', count)
