'''
@author: Nick DeMasi

Code to complete Day 14 of 2017 Advent of
Code using Python 3

'''

import re


def compare_16(num1, num2):
    '''Compares the last 16 bits of an integer'''
    bin1 = re.sub(r"^0b", "", bin(num1)).zfill(16)
    bin2 = re.sub(r"^0b", "", bin(num2)).zfill(16)

    if bin1[-16:] == bin2[-16:]:
        return True

    return False


class Generator(object):
    def __init__(self, factor, starting_value):
        self.factor = factor
        self.starting_value = starting_value
        self.value = starting_value

    def generate(self):
        '''Generates a new value according to the day 15 specs'''
        self.value = (self.value * self.factor) % 2147483647
        return self.value

    def reset(self):
        '''Resets current value to original starting value'''
        self.value = self.starting_value


if __name__ == '__main__':
    genA = Generator(16807, 873)
    genB = Generator(48271, 583)


    # count number of matches through 40,000,000 iterations
    matches = 0
    for i in range(40000000):
        if compare_16(genA.generate(), genB.generate()):
            matches += 1

    print("Part 1:        %d" % matches)


    # count the number of matches through 5,000,000 iterations
    # Generator A only returns a value when it is a multiple of 4
    # Generator B only returns a value when it is a multiple of 8

    # reset Generators
    genA.reset()
    genB.reset()

    # set-up variables
    matches = 0
    counter = 0
    genA_vals = []
    genB_vals = []

    # iterate through 5,000,000 pairs
    while counter < 5000000:
        if len(genA_vals) < 5000000:
            genA.generate()
            if genA.value % 4 == 0:
                genA_vals.append(genA.value)

        if len(genB_vals) < 5000000:
            genB.generate()
            if genB.value % 8 == 0:
                genB_vals.append(genB.value)

        if len(genA_vals) > counter and len(genB_vals) > counter:
            if compare_16(genA_vals[counter], genB_vals[counter]):
                matches += 1
            counter += 1

    print("Part 2:        %d" % matches)
