import os





def parse_fname(f_obj):
    """Parses the file name for get the day and year

    Returns day and year as ints
    """
    fname = str(f_obj).split('.')[0]
    _, day, year = fname.split('_')
    return int(day), int(year)


def read_input(year, day):
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
