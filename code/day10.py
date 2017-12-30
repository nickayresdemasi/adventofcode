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

    def reduce(self):
        '''Reduces a hash to a dense hash'''

        # create empty list to populate with dense hash
        self.dense_hash = []

        # iterate through array in groups of 16
        pos = 0
        while pos < len(self.circular_list.array):
            num = xor(self.circular_list.index(pos, pos + 16))
            self.dense_hash.append(num)
            pos += 16

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


    # create new lengths from ASCII
    lengths = [ord(c) for c in text]
    lengths += [17, 31, 73, 47, 23]

    # re-instantiate Knot Hash
    knot_hash.reset()

    for i in range(64):
        for l in lengths:
            knot_hash.tie(l)

    # create dense hash
    knot_hash.reduce()

    # convert to hexadecimal
    final_string = []
    for n in knot_hash.dense_hash:
        h = hex(n)
        final_string.append(h.replace('0x', ''))

    print("Part 2:          ", "".join(final_string))
