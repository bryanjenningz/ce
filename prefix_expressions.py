# Prefix Expressions
# Author: Bryan Jennings

# Given an input file with several lines consisting of 
# numbers and the operators +, *, and /. Calculate the values
# by using the last to the first operator on the numbers ordered
# first to last. For example, * + 2 3 4 evaluates to 20. 
# It evaluates (2 + 3) and then evaluates (5 * 4).

import sys

def op(operator, n1, n2):
    n1, n2 = float(n1), float(n2)
    if operator == '+':
        return n1 + n2
    elif operator == '*':
        return n1 * n2
    elif operator == '/':
        return n1 / n2

with open(sys.argv[1]) as file:
    lines = file.read().strip().split('\n')

for line in lines:
    numbers, operators = [], []
    for character in line.strip().split():
        if character in '+*/':
            operators.append(character)
        else:
            numbers.append(character)
    total = numbers[0]
    for n in range(1, len(numbers)):
        total = op(operators[len(operators) - n], total, numbers[n])
    print(int(total))
