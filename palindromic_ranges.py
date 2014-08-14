# Palindromic Ranges
# Author: Bryan Jennings

# 5, 77, 363, ... are palindromes.
# A range of integers is "interesting" if it contains an even 
# number of palindromes. Each line in an input file has 
# 2 numbers that represent the lower and upper bounds for the 
# range. Print the number of "interesting" subsets for each range.

import sys

def is_pal(number):
    return str(number) == str(number)[::-1]

def is_interesting(number_range):
    return sum(1 for number in number_range if is_pal(number)) % 2 == 0

def get_ranges(number_range):
    ranges = [number_range]
    for range_size in range(1, len(number_range)):
        for i in range(len(number_range) - range_size + 1):
            ranges.append(number_range[i:i + range_size])
    return ranges

with open(sys.argv[1], 'r') as file:
    lines = file.read().strip().split('\n')

for line in lines:
    interestings = 0
    lower, upper = (int(i) for i in (line.strip().split(' ')))
    for subset in get_ranges(range(lower, upper + 1)):
        if is_interesting(subset):
            interestings += 1
    print(interestings)
