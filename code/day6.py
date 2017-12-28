'''
@author: Nick DeMasi

Code to complete Day 6 of 2017 Advent of
Code using Python 3

'''

import os


ABS_PATH = 'C://Users/ldema/Coding/python_projects/adventofcode2017'


def reallocate(blocks):
    '''Finds largest number in sequence and reallocates all blocks in a
    left-to-right wrap-around cycle'''
    max_block = max(blocks)
    for i in range(len(blocks)):
        if blocks[i] == max_block:
            blocks[i] = 0
            index = i + 1
            break

    for i in range(max_block):
        if index >= len(blocks):
            index = 0
        blocks[index] += 1
        index += 1


if __name__ == '__main__':
    path = os.path.join(ABS_PATH, 'input/day6.txt')
    file = open(path, 'r')
    text = file.read()
    blocks = [int(n) for n in text.split('\t')]

    # save original view
    view = tuple(blocks)
    views = [view]
    counter = 0

    # reallocate until a view is repeated
    while True:
        reallocate(blocks)
        counter += 1
        view = tuple(blocks)
        if view in views:
            break
        views.append(view)

    # print answer to part 1
    print("Part 1:        ", counter)

    # save view which was repeated
    final_view = view

    # reset counter
    counter = 0

    # reallocate until final view is seen again
    while True:
        reallocate(blocks)
        counter += 1
        view = tuple(blocks)
        if view == final_view:
            break

    # print answer to part 2
    print("Part 2:        ", counter)
