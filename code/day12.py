'''
@author: Nick DeMasi

Code to complete Day 12 of 2017 Advent of
Code using Python 3

'''

import logging
import os
import re


ABS_PATH = 'C://Users/ldema/Coding/python_projects/adventofcode2017'


def subset(base_list, sub_list):
    '''Returns true or false if sub_list is indeed a subset of
    base_list'''
    for item in sub_list:
        if item not in base_list:
            return False

    return True


class Pipes(object):
    def __init__(self, text):
        self.pipes = self.__load(text)

    def __load(self, text):
        '''Loads a large string of text formatted in pipe style into a dict'''
        pipes = {}
        for p in text.split('\n'):
            base, cnxns = re.split('<->', p)
            base = int(base.strip())
            cnxns = [int(c.strip()) for c in cnxns.split(',')]
            pipes[base] = cnxns

        return pipes

    def count_connections(self, p_id, c_list=[]):
        '''Creates a list of connections to a specific pipe id'''
        # append initial pipe id
        c_list.append(p_id)
        logging.debug(c_list)

        # check if any connections have already been added
        if subset(c_list, self.pipes[p_id]):
            return c_list

        # run through multiple connections recursively
        for c in self.pipes[p_id]:

            # skip connections already found
            if c in c_list:
                continue

            c_list = self.count_connections(c, c_list=c_list)

        # return list of unique connections
        return c_list


if __name__ == '__main__':
    logging.basicConfig(filename='day12.log', filemode='w', level=logging.DEBUG)

    path = os.path.join(ABS_PATH, 'input/day12.txt')
    file = open(path, 'r')
    text = file.read()

    p = Pipes(text)
    print("Part 1:          ", len(p.count_connections(0)))
