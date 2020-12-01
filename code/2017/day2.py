'''
@author: Nick DeMasi

Code to complete Day 2 of 2017 Advent of
Code using Python 3

'''

import os


ABS_PATH = 'C://Users/ldema/Coding/python_projects/adventofcode2017'


def checksum(row):
    '''Calculates the difference between the max and min of numbers
    in a row of a spreadsheet'''
    diff = max(row) - min(row)
    return diff


def checksum_2(row):
    '''Finds two numbers in a spreadsheet which can be divided evenly
    into one another and returns the result of that division'''
    row.sort(reverse=True)

    for i in range(len(row)):
        for j in range(len(row) - 1, i, -1):
            if row[j] > row[i] / 2:
                break
            elif row[i] % row[j] == 0:
                return row[i] // row[j]

    return 0


if __name__ == '__main__':
    path = os.path.join(ABS_PATH, 'input/day2.txt')
    file = open(path, 'r')
    text = file.read()
    spreadsheet = [[int(n) for n in row.split('\t')] for row in text.split('\n')]

    total_1 = 0
    total_2 = 0
    for row in spreadsheet:
        total_1 += checksum(row)
        total_2 += checksum_2(row)
    print("Part 1:        ", total_1)
    print("Part 2:        ", total_2)
