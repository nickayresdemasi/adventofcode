import argparse
from importlib import import_module
import os


INPUT_DIR = os.path.join(os.path.dirname(__file__), "input")


def read_input(year, day):
    """Reads puzzle input

    Args:
        year (int): puzzle year
        day (int): puzzle day

    Returns:
        puzzle input as a string
    """
    fname = "day_{day}.txt".format(day=day, year=year)
    fpath = os.path.join(INPUT_DIR, str(year), fname)
    input_str = None
    with open(fpath, "r") as f:
        input_str = f.read()

    if input_str is None:
        raise IOError("Unable to read input")

    return input_str


def solve_puzzle(year, day, step=None):
    """Calls puzzle_solution function for the given year, day

    Args:
        year (int): puzzle year
        day (int): puzzle day

    Returns:
        None, prints solution to command line
    """
    puzzle_mod = import_module(f"src.puzzles.{year}.day_{day}")
    puzzle_input = read_input(year, day)
    if step:
        solution = getattr(puzzle_mod, f"puzzle_solution_{step}")(puzzle_input)
        print(f"{year} - Day {day} - Solution {step}: {solution}")
    else:
        solution_1 = getattr(puzzle_mod, f"puzzle_solution_1")(puzzle_input)
        print(f"{year} - Day {day} - Solution 1: {solution_1}")
        solution_2 = getattr(puzzle_mod, f"puzzle_solution_2")(puzzle_input)
        print(f"{year} - Day {day} - Solution 2: {solution_2}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="SolvePuzzle")
    parser.add_argument("year")
    parser.add_argument("day")
    parser.add_argument("-s", "--step")
    args = parser.parse_args()
    solve_puzzle(args.year, args.day, )
