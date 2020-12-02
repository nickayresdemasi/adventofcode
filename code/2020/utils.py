import os

from bs4 import BeautifulSoup
import requests


ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
INPUT_DIR = os.path.join(ROOT_DIR, "input")


def read_input(day, year):
    """Reads puzzle input

    Args:
        - day (int): puzzle day
        - year (int): puzzle year

    Returns a string
    """
    fname = "day_{day}_{year}.txt".format(day=day, year=year)
    fpath = os.path.join(INPUT_DIR, str(year), fname)
    input_str = None
    with open(fpath, "r") as f:
        input_str = f.read()

    if input_str is None:
        raise IOError("Unable to read input")

    return input_str


if __name__ == "__main__":
    print(read_input(1, 2020))
