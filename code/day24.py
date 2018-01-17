'''
@author: Nick DeMasi

Code to complete Day 24 of 2017 Advent of
Code using Python 3

'''


import logging
import os


ABS_PATH = 'C://Users/ldema/Coding/python_projects/adventofcode2017'


class Bridge(object):
    def __init__(self):
        self.max_length = 0
        self.max_strength = 0
        self.part_2 = 0

    def build_bridge(self, start, component_list, strength=0, length=0):
        '''Builds all possible bridges from given starting port, updates
        information on logest bridge and its strength and strongest bridge'''
        components, connections = self.__viable_components(start, component_list)
        if components:
            strength += start
            length += 1
            for x, c in zip(connections, components):
                temp = component_list.copy()
                temp.remove(c)
                self.build_bridge(x, temp, strength + x, length + 1)
        else:
            if strength >= self.max_strength:
                self.max_strength = strength
            if length >= self.max_length:
                self.max_length = length
                if strength > self.part_2:
                    self.part_2 = strength

    def __viable_components(self, x, component_list):
        '''Finds all viable connecting ports to current port x'''
        components = []
        connections = []
        for c in component_list:
            if x in c:
                components.append(c)
                temp = list(c)
                temp.remove(x)
                connections.append(temp[0])
        return components, connections


if __name__ == '__main__':
    logging.basicConfig(filename='day24.log', filemode='w', level=logging.DEBUG)
    # read in puzzle input
    path = os.path.join(ABS_PATH, 'input/day24.txt')
    file = open(path, 'r')
    text = file.read().split('\n')

    # create component list
    component_list = [tuple([int(n) for n in c.split('/')]) for c in text]

    # build bridges
    b = Bridge()
    b.build_bridge(0, component_list)

    print("Part 1:           %d" % b.max_strength)
    print("Part 2:           %d" % b.part_2)
