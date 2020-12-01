'''
@author: Nick DeMasi

Code to complete Day 12 of 2017 Advent of
Code using Python 3

'''


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

    def connections(self, p_id, c_list=[]):
        '''Creates a list of connections to a specific pipe id'''
        # append initial pipe id
        c_list.append(p_id)

        # check if any connections have already been added
        if subset(c_list, self.pipes[p_id]):
            return c_list

        # run through multiple connections recursively
        for c in self.pipes[p_id]:

            # skip connections already found
            if c in c_list:
                continue

            c_list = self.connections(c, c_list=c_list)

        # return list of unique connections
        return c_list

    def groups(self):
        '''Counts total number of self-contained groups in pipe map'''

        # create variable to track how many groups are seen
        groups = 0
        # create variable to track which pipes are already in groups
        used_pipes = []

        # iterate through pipes and check for new groups
        for k in self.pipes.keys():

            # skip pipes which have already been seen
            if k in used_pipes:
                continue

            used_pipes += self.connections(k)
            groups += 1

        return groups


if __name__ == '__main__':
    path = os.path.join(ABS_PATH, 'input/day12.txt')
    file = open(path, 'r')
    text = file.read()

    p = Pipes(text)
    print("Part 1:          ", len(p.connections(0)))
    print("Part 2:          ", p.groups())
