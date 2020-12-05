from math import ceil

from utils import parse_fname, read_input


DIRECTION_TRANSLATION = {'F': 1, 'B': 0, 'L': 1, 'R': 0}


def parse_input(input_str):
    boarding_passes = [
        [DIRECTION_TRANSLATION[d] for d in row]
        for row in input_str.split("\n")
        if row != ""
    ]
    return boarding_passes


def binary_search(num_items, search_directions):
    """Searches through a list of length num_items according to the search_directions

    Args:
        - num_items (int): number of items in the list
        - search_directions (list(int)): direction to search in, 1 is the front and
            0 is the back

    Returns the midpoint of the list
    """
    endpts = [0, num_items - 1]
    for sdir in search_directions[:-1]:
        mdpt = ceil((endpts[0] + endpts[1]) / 2)
        endpts[sdir] = mdpt - sdir
    return endpts[search_directions[-1] - 1]


def find_missing_seat(seat_ids, max_diff):
    """Takes a list of integers in ascending order, finds the midpoint between the
    first sequential pair whose difference exceeds max_diff

    Args:
        - seat_ids (list(int)): sorted list of integers
        - max_diff (int): maximum allowable difference between two sequential items

    Returns int
    """
    for i in range(len(seat_ids) - 1):
        if seat_ids[i + 1] - seat_ids[i] > max_diff:
            return seat_ids[i] + int((seat_ids[i + 1] - seat_ids[i]) / 2)
    return None


def main():
    input_str = read_input(*parse_fname(__file__))
    boarding_passes = parse_input(input_str)

    seat_ids = []
    for bpass in boarding_passes:
        r_id = binary_search(128, bpass[:7])
        c_id = binary_search(8, bpass[7:])
        seat_id = (r_id * 8) + c_id
        seat_ids.append(seat_id)
    print("PART 1")
    print("Max seat ID: %i" % max(seat_ids))
    print()

    seat_ids.sort()
    missing_seat_id = find_missing_seat(seat_ids, 1)
    print("PART 2")
    if missing_seat_id:
        print("Missing Seat ID: %i" % missing_seat_id)
    else:
        print("Missing seat not found")


if __name__ == '__main__':
    main()
