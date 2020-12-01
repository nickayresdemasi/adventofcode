'''
@author: Nick DeMasi

Code to complete Day 20 of 2017 Advent of
Code using Python 3

'''


import logging
import os
import re


ABS_PATH = 'C://Users/ldema/Coding/python_projects/adventofcode2017'


def manhattan_distance(coordinates):
    '''calculates the Manhattan Distance of coordinates'''
    return sum([abs(c) for c in coordinates])


def parse(line, component):
    '''Parses out acceleration components from day 20 input'''
    for element in line.split(' '):
        if element.startswith(component):
            coordinates = [int(g) for g in re.findall(r"-?[\d]+", element)]
            return coordinates


def remove_duplicates(d):
    '''removes all instances of duplicate key values from a dictionary'''
    duplicates = []
    values = list(d.values())
    for val in values:
        if values.count(val) > 1:
            duplicates.append(val)

    new_dict = {}
    for key, val in d.items():
        if val not in duplicates:
            new_dict[key] = val

    return new_dict


def simulate(particle, n):
    '''Simulates final Manhattan distance of particle after n iterations'''
    position = parse(particle, 'p')
    velocity = parse(particle, 'v')
    acceleration = parse(particle, 'a')

    final_position = []
    for p, v, a in zip(position, velocity, acceleration):
        final_position.append(p + (n * v) + ((n * (n + 1) * a) / 2))

    logging.debug(final_position)
    return tuple(final_position)


if __name__ == '__main__':
    logging.basicConfig(filename='day20.log', filemode='w', level=logging.DEBUG)
    # read in Puzzle input
    path = os.path.join(ABS_PATH, 'input/day20.txt')
    file = open(path, 'r')
    text = file.read().split('\n')

    # simulate distance after 100000 steps, return lowest distance
    min_distance = None
    min_particle = None

    for i, particle in enumerate(text):
        distance = manhattan_distance(simulate(particle, 100000))
        if not min_distance or distance < min_distance:
            min_distance = distance
            min_particle = i

    print("Part 1:           %s" % min_particle)

    # set up variables to complete part 2
    constant_iterations = 0
    n = 0
    particles = text
    num_particles = len(particles)

    while constant_iterations < 100:
        # create new dict to store particle postions
        logging.debug(n)
        temp_dict = {}
        for p in particles:
            temp_dict[p] = simulate(p, n)

        # remove from dictionary all instances of duplicated values
        temp_dict = remove_duplicates(temp_dict)

        # compare number of remaining particles
        if len(temp_dict) < num_particles:
            particles = temp_dict.keys()
            num_particles = len(particles)
            constant_iterations = 0
        else:
            constant_iterations += 1

        n += 1

    print("Part 2:           %s" % len(particles))
