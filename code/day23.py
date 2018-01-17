'''
@author: Nick DeMasi

Code to complete Day 23 of 2017 Advent of
Code using Python 3

'''


import os

from register import Register


ABS_PATH = 'C://Users/ldema/Coding/python_projects/adventofcode2017'

def is_prime(x):
    for i in range(2, x):
        if x % i == 0:
            return True
    return False

def translator(puzzle_input):
    '''Reads through puzzle input and translates into Register actions'''


    r = Register(0, 'abcdefgh')

    # set up tracking variables
    counter = 0
    mul = 0

    # iterate through instructions
    while counter < len(puzzle_input):
        # split instructions
        temp = puzzle_input[counter].split(' ')

        # convert sting digits to integers
        i_list = [x if x.isalpha() else int(x) for x in temp]

        # translate instructions
        if i_list[0] == 'set':
            r.set(i_list[1], i_list[2])
        elif i_list[0] == 'sub':
            r.sub(i_list[1], i_list[2])
        elif i_list[0] == 'mul':
            r.mul(i_list[1], i_list[2])
            mul += 1
        elif i_list[0] == 'jnz':
            if r.get_value(i_list[1]) != 0:
                counter += r.get_value(i_list[2]) - 1
        counter += 1

    print("Part 1:         %d" % mul)

    # perform caluclations for part 2
    h = 0
    for i in range(105700, 122700 + 1, 17):
        if is_prime(i):
            h += 1

    print("Part 2:         %d" % h)

if __name__ == '__main__':
    path = os.path.join(ABS_PATH, 'input/day23.txt')
    file = open(path, 'r')
    puzzle_input = file.read().split('\n')

    translator(puzzle_input)
