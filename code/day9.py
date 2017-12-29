'''
@author: Nick DeMasi

Code to complete Day 9 of 2017 Advent of
Code using Python 3

'''


import os


ABS_PATH = 'C://Users/ldema/Coding/python_projects/adventofcode2017'


class GroupParser(object):
    def __init__(self, user_input):
        self.input = user_input

    def group_calculator(self):
        '''Parses a string to calculate its total value based on
        the rules outlined in Day 9'''

        # definie initial tracker variables
        pos = 0
        stack = 0
        total = 0

        # initiate control loop
        while pos < len(self.input):
            c = self.input[pos]
            if c == '{':
                stack += 1
                pos += 1
            elif c == '}':
                if stack != 0:
                    total += stack
                    stack -= 1
                pos += 1
            elif c == '<':
                pos += self.garbage_time(pos)
            elif c == '!':
                pos += 2
            else:
                pos += 1

        return total

    def garbage_time(self, pos):
        '''Finds the end of a group of garbage'''
        offset = 1
        while self.input[pos + offset] != '>':
            offset += 1
            # check for nullifying character
            if self.input[pos + offset] == '!':
                offset += 1

        return offset


if __name__ == '__main__':
    path = os.path.join(ABS_PATH, 'input/day9.txt')
    file = open(path, 'r')
    text = file.read()

    gp = GroupParser(text)
    print("Part 1:         ", gp.group_calculator())
