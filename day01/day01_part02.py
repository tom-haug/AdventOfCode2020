import os
import sys


def find_nums_sum_to_expected(lines, expected):
    for num1 in lines:
        for num2 in lines:
            for num3 in lines:
                sum = int(num1) + int(num2) + int(num3)
                if sum == expected:
                    return [int(num1), int(num2), int(num3)]


filePath = os.path.join(sys.path[0], "input.txt")
searchSum = 2020

f = open(filePath, "r")
inputContent = f.read()
lines = inputContent.split("\n")

num1, num2, num3 = find_nums_sum_to_expected(lines, searchSum)

print(num1)
print(num2)
print(num3)
print(num1 * num2 * num3)