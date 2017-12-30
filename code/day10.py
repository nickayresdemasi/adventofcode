'''
@author: Nick DeMasi

Code to complete Day 10 of 2017 Advent of
Code using Python 3

'''


import os


ABS_PATH = 'C://Users/ldema/Coding/python_projects/adventofcode2017'


class CircularList(object):
    def __init__(self, array):
        self.array = array

    def index(self, beg, end):
        '''Allows for indexing of circular list'''

        # check that index is entered correctly
        if beg > end:
            raise ValueError("Invalid indexing")

        # wrap-around if necessary
        if end > len(self.array):
            first_half = self.array[beg:]
            second_half = self.array[:end - len(self.array)]
            sub = first_half + second_half
        else:
            sub = self.array[beg:end]

        return sub

    def replace(self, beg, sub):
        '''Allows for replacement of portion of circular list with other list'''

        for i in range(len(sub)):
            index = beg + i

            # wrap-around if index outside range of array
            if index >= len(self.array):
                index %= len(self.array)

            self.array[index] = sub[i]


if __name__ == '__main__':
    path = os.path.join(ABS_PATH, 'input/day10.txt')
    file = open(path, 'r')
    lengths = [int(n) for n in file.read().split(',')]

    # instantiate circular list
    clist = CircularList([i for i in range(256)])

    # instantiate trakcer variables for list position and skip size
    pos = 0
    skip = 0

    # iterate through lengths
    for l in lengths:
        # identify end of list
        end = pos + l

        # create sub-array and reverse
        sub = clist.index(pos, end)
        reverse = sub[::-1]

        # replace all values
        clist.replace(pos, reverse)

        # move position
        pos = end + skip
        if pos >= len(clist.array):
            pos %= len(clist.array)

        # increase skip size
        skip += 1

    print("Part 1:          ", clist.array[0] * clist.array[1])
