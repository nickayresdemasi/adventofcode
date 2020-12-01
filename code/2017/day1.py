'''
@author: Nick DeMasi

Code to complete Day 1 of 2017 Advent of
Code using Python 3

'''

import os


ABS_PATH = 'C://Users/ldema/Coding/python_projects/adventofcode2017'


def calculate(number):
    '''Calculates the sum of all digits in a sequence which match
    the preceding digit.'''
    total = 0
    digits = len(number)
    for i in range(digits):
        if number[i] == number[(i + 1) % digits]:
            total += int(number[i])

    return total


def calc_by_half(number):
    '''Calculates the sum of all digits in a sequence which match
    the digit half the distance away from it in the sequence.'''
    total = 0
    digits = len(number)
    step = digits // 2
    for i in range(digits):
        if number[i] == number[(i + step) % digits]:
            total += int(number[i])

    return total


if __name__ == '__main__':
    path = os.path.join(ABS_PATH, "input/day1.txt")
    file = open(path, 'r')
    number = file.read()
    total_1 = calculate(number)
    total_2 = calc_by_half(number)
    print("Part 1:         {}".format(total_1))
    print("Part 2:         {}".format(total_2))
