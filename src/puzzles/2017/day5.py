'''
@author: Nick DeMasi

Code to complete Day 5 of 2017 Advent of
Code using Python 3

'''

import os


ABS_PATH = 'C://Users/ldema/Coding/python_projects/adventofcode2017'


def exit_array_simple(array):
    '''Exits an array of numbers following simple rules'''
    pos = 0
    moves = 0
    while pos < len(array):
        jump = array[pos]
        array[pos] += 1
        pos += jump
        moves += 1

    return moves


def exit_array_complex(array):
    '''Exits an array of numbers folliwng complex rules'''
    pos = 0
    moves = 0
    while pos < len(array):
        jump = array[pos]
        if jump >= 3:
            array[pos] -= 1
        else:
            array[pos] += 1
        pos += jump
        moves += 1

    return moves


if __name__ == '__main__':
    path = os.path.join(ABS_PATH, 'input/day5.txt')
    file = open(path, 'r')
    text = file.read()
    nums = [int(n) for n in text.split('\n')]

    print("Part 1:        ", exit_array_simple(nums))
    print("Part 2:        ", exit_array_complex(nums))
