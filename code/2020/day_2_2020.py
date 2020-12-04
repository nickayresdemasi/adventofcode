from utils import read_input


def parse_input(input_str):
    rows = [r.split(':') for r in input_str.split('\n') if r != '']
    criteria, passwords = [r[0] for r in rows], [r[1] for r in rows]
    passwords = [p.strip() for p in passwords]
    criteria = [c.split(' ') for c in criteria]
    criteria = [
        (int(c[0].split('-')[0]), int(c[0].split('-')[1]),  c[1])
        for c in criteria
    ]
    return criteria, passwords


def method_1(lowr, uppr, letter, password):
    """letter must occur between lowr and uppr times in password

    Args:
        - lowr (int): lower limit on occurences of letter in password
        - uppr (int); upper limit on occurences of letter in password
        - letter (str): letter that must appear in password
        - passwod (str)

    Returns 1 if password conforms to criteria, 0 if not
    """
    return lowr <= len([l for l in password if l == letter]) <= uppr


def method_2(lowr, uppr, letter, password):
    """letter must occur once at either lowr or uppr index in password. 1-index

    Args:
        - lowr (int): lower index
        - uppr (int); upper index
        - letter (str): letter that must appear in password
        - passwod (str)

    Returns 1 if password conforms to criteria, 0 if not
    """
    return ((password[lowr - 1] == letter) + (password[uppr - 1] == letter)) == 1


def find_valid_passwords(criteria, passwords, method):
    """finds valid passwords that comply to the criteria and method

    Args:
        - criteria (list(tuple(int, int, str))): input passed to method
        - passwords (list(str))
        - method (func): function that takes criteria as input and returns 1 or 0

    Returns the number of valid passwords that comply to the criteria and method
    """
    if len(criteria) != len(passwords):
        raise ValueError('list of criteria and list of passwords must be same length')

    valid_passwords = 0
    for c, p in zip(criteria, passwords):
        lowr, uppr, letter = c
        valid_passwords += method(lowr, uppr, letter, p)
    return valid_passwords


def main():
    # read input
    input_str = read_input(2, 2020)
    criteria, passwords = parse_input(input_str)

    # part 1
    valid_passwords = find_valid_passwords(criteria, passwords, method_1)
    print("PART 1")
    print("Valid Passwords: %i" % valid_passwords)
    print()

    # part 1
    valid_passwords = find_valid_passwords(criteria, passwords, method_2)
    print("PART 2")
    print("Valid Passwords: %i" % valid_passwords)


if __name__ == '__main__':
    main()
