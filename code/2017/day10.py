'''
@author: Nick DeMasi

Code to complete Day 10 of 2017 Advent of
Code using Python 3

'''


import os

from circular_list import CircularList


ABS_PATH = 'C://Users/ldema/Coding/python_projects/adventofcode2017'


def xor(l):
    if len(l) <= 1:
        raise TypeError("List must be longer than size 1")

    result = l[0] ^ l[1]
    if len(l) > 2:
        for c in l[2:]:
            result = result ^ c

    return result


class KnotHash(object):
    def __init__(self):
        self.circular_list = CircularList([i for i in range(256)])
        self.pos = 0
        self.skip = 0

    def create_hash(self, s):
        '''Creates a knot hash from a string of input'''

        # create lengths from ASCII conversions
        knot_lengths = [ord(c) for c in s]
        # append standard end lengths
        knot_lengths += [17, 31, 73, 47, 23]

        # perform ties of each lenght 64 times
        for i in range(64):
            for l in knot_lengths:
                self.tie(l)

        # reduce hash to dense hash
        dense_hash = self.__reduce()

        # create and return final string of hex values
        final_string = []
        for n in dense_hash:
            h = hex(n)
            final_string.append(h.replace('0x', '').zfill(2))

        return ''.join(final_string)

    def reset(self):
        '''Resets position and skip to 0'''
        self.circular_list = CircularList([i for i in range(256)])
        self.pos = 0
        self.skip = 0

    def tie(self, length):
        '''Reverse portion of array for user-passed length, increases positiona
        and skip tracker variables'''

        # identify end of list
        end = self.pos + length

        # creat sub-array and reverse
        sub = self.circular_list.index(self.pos, end)
        reverse = sub[::-1]

        # replace all values
        self.circular_list.replace(self.pos, reverse)

        # move position
        self.pos = end + self.skip
        if self.pos > len(self.circular_list.array):
            self.pos %= len(self.circular_list.array)

        # increase skip size
        self.skip += 1

    def __reduce(self):
        '''Reduces a hash to a dense hash'''

        # create empty list to populate with dense hash
        dense_hash = []

        # iterate through array in groups of 16
        pos = 0
        while pos < len(self.circular_list.array):
            num = xor(self.circular_list.index(pos, pos + 16))
            dense_hash.append(num)
            pos += 16

        return dense_hash


if __name__ == '__main__':
    path = os.path.join(ABS_PATH, 'input/day10.txt')
    file = open(path, 'r')
    text = file.read()

    # create lengths from text
    lengths = [int(n) for n in text.split(',')]

    # instantiate Knot Hash
    knot_hash = KnotHash()

    # iterate through lengths
    for l in lengths:
        knot_hash.tie(l)

    print("Part 1:          ", knot_hash.circular_list.array[0] * knot_hash.circular_list.array[1])

    # reset Knot Hash
    knot_hash.reset()

    # create true knot hash treating list of numbers as a string
    print("Part 2:          ", knot_hash.create_hash(text))
