"""Advent of Code Day 3 2023"""

import re


def safe_index(matrix, m, n):
    """Safely index a limited matrix"""
    try:
        return matrix[n][m]
    except:
        # return empty space if outside bounds of matrix
        # empty space represented by "."
        return "."


def get_full_number(matrix, m, n):
    """Returns the full number based on position of a single digit"""
    number = [safe_index(matrix, m, n)]
    # look left
    m_l = m - 1
    c = safe_index(matrix, m_l, n)
    while c.isnumeric():
        number.insert(0, c)
        m_l -= 1
        c = safe_index(matrix, m_l, n)
    # look right
    m_r = m + 1
    c = safe_index(matrix, m_r, n)
    while c.isnumeric():
        number.insert(len(number), c)
        m_r += 1
        c = safe_index(matrix, m_r, n)
    return int("".join(number))


def is_symbol(matrix, m , n):
    c = safe_index(matrix, m, n)
    if c.isnumeric() or c == ".":
        return ""
    else:
        return c


def is_number(matrix, m, n):
    if safe_index(matrix, m, n).isnumeric():
        return get_full_number(matrix, m, n)
    else:
        return ""


def look_around(matrix, m, n, is_search_target):
    acquired_targets = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            c = is_search_target(matrix, m+i, n+j)
            if c:
                acquired_targets.append(c)
    return acquired_targets


def puzzle_solution_1(engine_schema):
    engine_schema = engine_schema.strip().split("\n")
    M = len(engine_schema[0])

    checksum = 0
    number = []
    symbols = []
    for n, line in enumerate(engine_schema):
        for m, c in enumerate(line):
            if c.isnumeric():
                number.append(c)
                symbols.extend(look_around(engine_schema, m, n, is_symbol))
            elif number and (m == M - 1 or not c.isnumeric()):
                checksum += int("".join(number)) if symbols else 0
                number = []
                symbols = []


    return checksum


def puzzle_solution_2(engine_schema):
    engine_schema = engine_schema.strip().split("\n")

    checksum = 0
    for n, line in enumerate(engine_schema):
        for m, c in enumerate(line):
            if c != "*":
                continue
            numbers = list(set(look_around(engine_schema, m, n, is_number)))
            if len(numbers) == 2:
                checksum += numbers[0] * numbers[1]

    return checksum


if __name__ == "__main__":
    puzzle_input = "\n".join([
        "467..114..",
        "...*......",
        "..35..633.",
        "......#...",
        "617*......",
        ".....+.58.",
        "..592.....",
        "......755.",
        "...$.*....",
        ".664.598.."
    ])
    ps_1 = puzzle_solution_1(puzzle_input)
    ps_2 = puzzle_solution_2(puzzle_input)
    print("Puzzle #: Expected - Received")
    print(f"1: 4361 - {ps_1}")
    print(f"2: 467835 - {ps_2}")
