"""Advent of Code 2023, Day 9"""

from functools import reduce


def process_puzzle_input(puzzle_input: str) -> list[list[int]]:
    sequences = [
        [int(x) for x in row.split(" ")]
        for row in puzzle_input.strip().split("\n")
    ]
    return sequences


def difference_sequence(S):
    return [S[i + 1] - S[i] for i in range(len(S) - 1)]


def sequence_of_zeros(S):
    return True if sum([bool(s) for s in S]) == 0 else False


def puzzle_solution_1(puzzle_input: str) -> int:
    sequences = process_puzzle_input(puzzle_input)
    checksum = 0
    for S in sequences:
        if sequence_of_zeros(S):
            continue
        last_vals = [S[-1]]
        differences = difference_sequence(S)
        while not sequence_of_zeros(differences):
            last_vals.append(differences[-1])
            differences = difference_sequence(differences)
        checksum += sum(last_vals)
    return checksum


def puzzle_solution_2(puzzle_input: str) -> int:
    sequences = process_puzzle_input(puzzle_input)
    checksum = 0
    for S in sequences:
        if sequence_of_zeros(S):
            continue
        first_vals = [S[0]]
        differences = difference_sequence(S)
        while not sequence_of_zeros(differences):
            first_vals.insert(0, differences[0])
            differences = difference_sequence(differences)
        checksum += reduce(lambda a, b: b - a, first_vals)
    return checksum


if __name__ == "__main__":
    ex_puzzle_input = "\n".join([
        "0 3 6 9 12 15",
        "1 3 6 10 15 21",
        "10 13 16 21 30 45",
    ])
    print("Puzzle #: Expected - Received")
    ps_1 = puzzle_solution_1(ex_puzzle_input)
    print(f"1: 114 - {ps_1}")
    ps_2 = puzzle_solution_2(ex_puzzle_input)
    print(f"2: 2 - {ps_2}")
