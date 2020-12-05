import re

from utils import parse_fname, read_input


def parse_input(input_str):
    passports = [
        row.replace('\n', ' ')
        for row in input_str.split('\n\n')
        if row != ''
    ]
    passports = [
        {m[1]: m[2] for m in re.findall(r'(\b([a-z]{3}):([^\s]+)\b)', passport)}
        for passport in passports
    ]
    return passports


def hgt_validation(value):
    m = re.match(r'^([\d]+)(cm|in)$', value)
    if m is None:
        return False
    if m.group(2) == 'cm':
        return 150 <= int(m.group(1)) <= 193
    else:
        return 59 <= int(m.group(1)) <= 76


FIELDS = {
    'byr': lambda v: 1920 <= int(v) <= 2002 if v.isdigit() else False,
    'iyr': lambda v: 2010 <= int(v) <= 2020 if v.isdigit() else False,
    'eyr': lambda v: 2020 <= int(v) <= 2030 if v.isdigit() else False,
    'hgt': hgt_validation,
    'hcl': lambda v: bool(re.match(r'^#[a-f0-9]{6}$', v)),
    'ecl': lambda v: v in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
    'pid': lambda v: len(v) == 9 if v.isdigit() else False,
    'cid': lambda v: True
}


def is_valid(passport, optional=[], validate_data=False):
    """Confirms if a password is valid based on presence of ids or on correct data

    Args:
        - passport (dict): ids and the data associated with them
        - optional (list): ids that should be ignored
        - validate_data (bool): whether to check if the data is valid is not

    Returns a bool
    """
    if validate_data:
        mtchs = [
            FIELDS.get(k, lambda _v: False)(v)
            for k, v in passport.items()
            if k not in optional
        ]
    else:
        mtchs = [
            k in FIELDS
            for k in passport.keys()
            if k not in optional
        ]
    return all(mtchs) and len(mtchs) == (len(FIELDS) - len(optional))


def main():
    input_str = read_input(*parse_fname(__file__))
    passports = parse_input(input_str)

    valid_passports = 0
    for passport in passports:
        valid_passports += is_valid(passport, optional=['cid'])
    print("PART 1")
    print("Valid passorts: %i" % valid_passports)
    print()

    valid_passports = 0
    for passport in passports:
        valid_passports += is_valid(passport, optional=['cid'], validate_data=True)
    print("PART 2")
    print("Valid passports: %i" % valid_passports)


if __name__ == '__main__':
    main()
