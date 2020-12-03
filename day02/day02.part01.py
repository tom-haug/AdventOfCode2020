import os
import sys
import re


def build_password_list(lines):
    regex = re.compile("(\d+)-(\d+)\s(\w):\s(\w+)")
    passwords = []
    for line in lines:
        match = regex.match(line)
        min, max, expected_char, password = match.group(1, 2, 3, 4)
        occurances = [m for m in re.findall(expected_char, password)]
        passwords.append((int(min), int(max), expected_char, password, len(occurances)))
    return passwords


filePath = os.path.join(sys.path[0], "input.txt")
f = open(filePath, "r")
inputStr = f.read()
lines = inputStr.split("\n")
passwords = build_password_list(lines)
print('All Passwords', passwords)

valid_passwords = [password for password in passwords if password[0] <= password[4] <= password[1]]

print('Valid Passwords', valid_passwords)
print('Num Valid: ', len(valid_passwords))