import os
import sys


def find_nums_sum_to_expected(lines, expected):
    for num1 in lines:
        for num2 in lines:
            sum = int(num1) + int(num2)
            if sum == expected:
                return [int(num1), int(num2)]


filePath = os.path.join(sys.path[0], "input.txt")
searchSum = 2020

f = open(filePath, "r")
input = f.read()
lines = input.split("\n")

num1, num2 = find_nums_sum_to_expected(lines, searchSum)

print(num1)
print(num2)
print(num1 * num2)