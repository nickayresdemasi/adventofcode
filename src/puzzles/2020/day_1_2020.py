from utils import read_input


def parse_input(input_str):
    return [int(v) for v in input_str.split("\n") if v.isdigit()]


def find_two_num(ledger, checksum):
    """Finds two numbers in an ordered list whose sum is equal to another number

    Args:
        - ledger (list(int)): list of integers in ascending order
        - checksum (int): The target sum

    Returns int, int if successful and None, None if not
    """
    if len(ledger) < 2:
        return None, None

    v1 = ledger.pop(0)
    rem = checksum - v1
    while len(ledger) >= 1:
        v2 = ledger[-1]
        if v2 == rem:
            return v1, v2
        elif v2 < rem:
            return find_two_num(ledger, checksum)
        del ledger[-1]
    return None, None


def find_three_num(ledger, checksum):
    """Finds three numbers in an ordered list whose sum is equal to another number

    Args:
        - ledger (list(int)): list of integers in ascending order
        - checksum (int): The target sum

    Returns int, int, int if successful and None, None, None if not
    """
    while len(ledger) >= 3:
        v1 = ledger.pop(0)
        if v1 + ledger[0] > checksum:
            break
        temp_checksum = checksum - v1
        v2, v3 = find_two_num(ledger.copy(), temp_checksum)
        if v2 and v3:
            return v1, v2, v3
    return None, None, None


def main():
    input_str = read_input(1, 2020)
    # parse and sort ledger
    ledger = parse_input(input_str)
    ledger.sort()
    # set checksum
    checksum = 2020

    # find two numbrs
    print("PART 1:")
    v1, v2 = find_two_num(ledger.copy(), checksum)
    if v1 and v2:
        print("2020 = {v1} + {v2}".format(v1=v1, v2=v2))
        print("{v1} * {v2} = {prod}".format(v1=v1, v2=v2, prod=v1 * v2))
    else:
        print("No solution found")
    print()

    # find three numbers
    print("PART 2:")
    v1, v2, v3 = find_three_num(ledger.copy(), checksum)
    if v1 and v2 and v3:
        print("2020 = {v1} + {v2} + {v3}".format(v1=v1, v2=v2, v3=v3))
        prod = v1 * v2 * v3
        print("{v1} * {v2} * {v3} = {prod}".format(v1=v1, v2=v2, v3=v3, prod=prod))
    else:
        print("No solution found")


if __name__ == "__main__":
    main()
