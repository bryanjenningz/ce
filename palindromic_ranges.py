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

def is_interesting(n_range):
    if len(n_range) == 0: return False
    number_pals = 0
    for number in n_range:
        if is_pal(number): number_pals += 1
    return number_pals % 2 == 0

def get_ranges(n_range):
    ranges = [n_range]
    for range_size in range(1, len(n_range)):
        for i in range(len(n_range) - range_size + 1):
            ranges.append(n_range[i:i + range_size])
    return ranges

with open(sys.argv[1], 'r') as file:
    lines = file.read().strip().split('\n')

for line in lines:
    interestings = 0
    L, R = line.strip().split(' ')
    L, R = int(L), int(R)
    for r in get_ranges(range(L, R+1)):
        if is_interesting(r):
            interestings += 1
    print(interestings)
