from collections import Counter

from utils import parse_fname, read_input


def parse_input(input_str):
    return [row.split("\n") for row in input_str.split("\n\n") if row != ""]


def valid_questions(questions_answered, min_answered):
    """Calculates the number of valid questions answered by a group of people
    based on the minimum threshold of those that answered

    Args:
        - questions_answered (list(iteable)): list of questions answered
        - min_answered (int): minimum number of a times a question had to have been
            answered to be considered valid

    Returns the number of valid questions as int
    """
    c = Counter()
    for ansr in questions_answered:
        c.update(ansr)
    return sum([1 for k in c.keys() if c[k] >= min_answered])


def main():
    input_str = read_input(*parse_fname(__file__))
    groups = parse_input(input_str)

    all_valid_questions = sum([valid_questions(grp, 1) for grp in groups])
    print("PART 1")
    print("Valid questions: %i" % all_valid_questions)
    print()

    all_valid_questions = sum([valid_questions(grp, len(grp)) for grp in groups])
    print('PART 2')
    print("Valid questions: %i" % all_valid_questions)


if __name__ == '__main__':
    main()
