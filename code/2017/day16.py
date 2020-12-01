'''
@author: Nick DeMasi

Code to complete Day 16 of 2017 Advent of
Code using Python 3

'''


import os
import re
import string


ABS_PATH = 'C://Users/ldema/Coding/python_projects/adventofcode2017'


def dance(sequence, instructions):
    '''function to implement all dance moves on a sequence'''

    # instantiate DancingList
    dl = DancingList([c for c in sequence])

    # iterate through and execute instructions
    for s in instructions:
        if s.startswith('s'):
            x = int(s[1:])
            dl.spin(x)
        elif s.startswith('x'):
            index1, index2 = s[1:].split('/')
            dl.iswap(int(index1), int(index2))
        elif s.startswith('p'):
            item1, item2 = s[1:].split('/')
            dl.swap(item1, item2)

    return "".join(dl.iterable)


class DancingList(object):
    def __init__(self, iterable):
        self.iterable = iterable

    def iswap(self, index1, index2):
        '''Swaps list item at index 1 with list item at index 2'''
        item1, item2 = self.iterable[index1], self.iterable[index2]
        self.iterable[index1], self.iterable[index2] = item2, item1

    def spin(self, x):
        '''Moves x-number of list items from the end to the front'''
        beg = self.iterable[:-x]
        end = self.iterable[-x:]
        self.iterable = end + beg

    def swap(self, item1, item2):
        '''swaps item 1 in list with item 2 in list'''
        index1 = self.__return_index(item1)
        index2 = self.__return_index(item2)
        self.iswap(index1, index2)

    def __return_index(self, p_item):
        '''private method which returns the first index position of the given
        item in the list'''
        for i, item in enumerate(self.iterable):
            if item == p_item:
                return i


if __name__ == '__main__':
    # read in puzzle input
    path = os.path.join(ABS_PATH, 'input/day16.txt')
    file = open(path, 'r')
    instructions = file.read().split(',')

    sequence = string.ascii_lowercase[:16]

    print("Part 1:            %s" % dance(sequence, instructions))

    seen = []
    for i in range(1000000000):

        # skip over sequences already seen
        if sequence in seen:
            print("Part 2:            %s" % seen[1000000000 % i])
            break

        # append new sequence
        seen.append(sequence)

        # perform dance and log mapping
        sequence = dance(sequence, instructions)
