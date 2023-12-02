'''
@author: Nick DeMasi

Code to complete Day 17 of 2017 Advent of
Code using Python 3

'''




def circular_insert(l, steps, cycles):
    '''Implements spinlock insertion protocol for day 17'''
    pos = 0
    for i in range(1, cycles + 1):
        index = ((steps + pos) % i) + 1
        l.insert(index, i)
        pos = index

    return pos


if __name__ == '__main__':
    # define beginning list and number of steps
    l = [0]
    steps = 349

    # begin circular insertion
    pos = circular_insert(l, steps, 2017)
    print("Part 1:            ", l[pos + 1])

    # we only care about when the index == 1 for part 2
    answer = 0
    for i in range(1, 50000001):
        index = ((349 + pos) % i) + 1
        if index == 1:
            answer = i
        pos = index

    print("Part 2:            ", answer)
