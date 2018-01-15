'''
@author: Nick DeMasi

Code to complete Day 21 of 2017 Advent of
Code using Python 3

'''


import os

import numpy as np


ABS_PATH = 'C://Users/ldema/Coding/python_projects/adventofcode2017'


def split(grid):
    '''Splits a grid into a seires of sub grids depending on if
    it is divisible by 2 or 3'''

    # check if grid is divisible by 2 or 3
    if len(grid) % 2 == 0:
        split_by = 2
    elif len(grid) % 3 == 0:
        split_by = 3

    # create empty list to store sub grids
    split_grid = []

    # divide grid into sub grids
    m_floor = 0
    for m in range(split_by,len(grid) + 1,split_by):
        n_floor = 0
        for n in range(split_by,len(grid) + 1,split_by):
            sub_grid = grid[m_floor:m, n_floor:n]
            split_grid.append(sub_grid)
            n_floor = n
        m_floor = m

    return split_grid

def transform(grid, translation_dict):
    '''Checks all permutations to see if grid can be translated'''
    for p in __permutations(grid):
        t = __convert_to_tuple(p)
        if t in translation_dict.keys():
            return np.array([[j for j in i] for i in translation_dict[t]])

def __convert_to_tuple(grid):
    '''Converts a 2-d numpy array to a 2-d tuple'''
    t = tuple(["".join([j for j in i]) for i in grid])
    return t

def __permutations(grid):
    '''Creates array of 8 possible permutations'''
    permutations = []
    for g in [grid, np.flip(grid, 1)]:
        for i in range(4):
            permutations.append(np.rot90(g, i))
    return permutations


def join(grids):
    join_by = int(float(len(grids)) ** (1 / 2))

    joined_grid = []

    floor = 0
    for i in range(join_by,len(grids) + 1,join_by):
        joined_grid.append(np.hstack(tuple(grids[floor:i])))
        floor = i

    return np.vstack(tuple(joined_grid))


if __name__ == '__main__':
    path = os.path.join(ABS_PATH, 'input/day21.txt')
    file = open(path, 'r')
    text = file.read().split('\n')

    # create translation dict
    translation_dict = {}
    for entry in text:
        k, v = entry.split('=>')
        translation_dict[tuple(k.strip().split('/'))] = tuple(v.strip().split('/'))

    # create initial grid
    grid = np.array([[j for j in i] for i in ('.#.', '..#', '###')])

    # go through 5 expansions
    for i in range(18):
        grids = []
        split_grid = split(grid)
        for g in split_grid:
            grids.append(transform(g, translation_dict))
        grid = join(grids)
        if i == 4:
            # count and return all used spaces
            unique, counts = np.unique(grid, return_counts=True)
            d = dict(zip(unique, counts))
            part_1 = d['#']

    # count and return all used spaces
    unique, counts = np.unique(grid, return_counts=True)
    d = dict(zip(unique, counts))
    print("Part 1:            %d" % part_1)
    print("Part 2:            %d" % d['#'])
