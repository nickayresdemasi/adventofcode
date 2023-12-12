"""Advent of Code 2023, Day 6"""

from math import ceil, floor
import re


def process_puzzle_input(puzzle_input: str) -> list[tuple[int]]:
    t, d = puzzle_input.strip().split("\n")
    t = [int(ms) for ms in re.findall(r"\d+", t)]
    d = [int(mm) for mm in re.findall(r"\d+", d)]
    races = [(ms, mm) for ms, mm in zip(t, d)]
    return races


def ways_to_win(t, d):
    ways_to_win = (
        ceil((t + (t**2 - 4 * d)**0.5) / 2)
        - floor((t - (t**2 - 4 * d)**0.5) / 2)
        - 1
    )
    return ways_to_win


def puzzle_solution_1(puzzle_input: str) -> int:
    races = process_puzzle_input(puzzle_input)

    checksum = 1
    for race in races:
        t, d = race
        checksum *= ways_to_win(t, d)

    return checksum


def puzzle_solution_2(puzzle_input: str) -> int:
    races = process_puzzle_input(puzzle_input)
    t = int("".join([str(race[0]) for race in races]))
    d = int("".join([str(race[1]) for race in races]))

    checksum = ways_to_win(t, d)

    return checksum


if __name__ == "__main__":
    ex_puzzle_input = "\n".join([
        "Time:      7  15   30",
        "Distance:  9  40  200"
    ])
    print("Puzzle #: Expected - Received")
    ps_1 = puzzle_solution_1(ex_puzzle_input)
    print(f"1: 288 - {ps_1}")
    ps_2 = puzzle_solution_2(ex_puzzle_input)
    print(f"2: 71503 - {ps_2}")
