'''
@author: Nick DeMasi

Code to complete Day 12 of 2017 Advent of
Code using Python 3

'''


import os


ABS_PATH = 'C://Users/ldema/Coding/python_projects/adventofcode2017'


class Firewall(object):
    def __init__(self, text):
        self.layers = self.__load(text)

    def severity(self, delay=0):
        '''Calculates the severity of a packet's trip through the
        firewall'''

        severity = 0
        caught = 0

        # iterate through all layers and check for interference
        for k in self.layers.keys():
            time = k + delay
            scan = self.layers[k]
            check_val = (scan - 1) * 2
            if time % check_val == 0:
                severity += k * scan
                caught += 1

        return severity, caught

    def __load(self, text):
        '''Constructs a dictionary mapping layer number to scanning
        depth'''
        layers = {}
        for l in text.split('\n'):
            layer, scan = l.split(':')
            layers[int(layer.strip())] = int(scan.strip())

        return layers


if __name__ == '__main__':
    # read in puzzle input
    path = os.path.join(ABS_PATH, 'input/day13.txt')
    file = open(path, 'r')
    text = file.read()

    # instantiate firewall
    f = Firewall(text)

    # calculate severity
    print("Part 1:          ", f.severity()[0])

    # calculate minimum seconds to delay
    delay = 0
    while True:
        if f.severity(delay=delay)[1] == 0:
            break
        delay += 1

    print("Part 2:          ", delay)
