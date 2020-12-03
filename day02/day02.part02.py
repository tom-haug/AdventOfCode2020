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


filePath = os.path.join(sys.path[0], "input.txt")
f = open(filePath, "r")
inputStr = f.read()
lines = inputStr.split("\n")
passwords = build_password_list(lines)
print('All Passwords', passwords)

valid_passwords = [password for password in passwords
                   if (password[3][password[0] - 1] == password[2]) !=
                   (password[3][password[1] - 1] == password[2])]

print('Valid Passwords', valid_passwords)
print('Num Valid: ', len(valid_passwords))