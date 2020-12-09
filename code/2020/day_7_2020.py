from collections import defaultdict
import re

from utils import parse_fname, read_input


BAG_PATTERN = r'^([\d]+) (.+)(?=bag|bags)'


def parse_input(input_str):
    rows = [row.split("contain") for row in input_str.split("\n") if row != ""]
    containing = defaultdict(dict)
    contained_by = defaultdict(list)
    for row in rows:
        container = row[0].replace("bags", "").strip()
        if row[1].strip() == "no other bags.":
            continue
        contents = [re.match(BAG_PATTERN, c.strip()) for c in row[1].split(",")]
        for m in contents:
            containing[container].update({m.group(2).strip(): int(m.group(1))})
            contained_by[m.group(2).strip()].append(container)
    return containing, contained_by


def find_all_containers(bags, color):
    """Finds all bags that can contain bag of bag_color

    Args:
        - bags (dict(list)): keys are bag colors and values are lists of bags that
            can contain them
        - color (str): color of bag you are finding containers of

    Returns set of all bag colors that can contain bag of bag_color"""
    containers = set(bags[color])
    for container in bags[color]:
        containers.update(find_all_containers(bags, container))
    return containers


def find_all_contained(bags, color, multiplier=1):
    """Finds number of bags contained by a bag of color

    Args:
        - bags (dict(dict)): keys of inner and outer dictionary are bag colors, outer
            bag colors contain inner bag colors in the amount of value of inner value
        - color (str): color of bag you are counting inside
        - multiplier (int): number of bags of color you are counting inside

    Returns int of bags cotained by bag of color
    """
    bags_contained = sum([multiplier * v for v in bags[color].values()])
    for container, amount in bags[color].items():
        bags_contained += find_all_contained(
            bags, container, multiplier=amount * multiplier
        )
    return bags_contained


def main():
    input_str = read_input(*parse_fname(__file__))
    containing, contained_by = parse_input(input_str)

    containers = len(find_all_containers(contained_by, "shiny gold"))
    print("PART 1")
    print("Can be contained by %i bags" % containers)
    print()

    bags_contained = find_all_contained(containing, "shiny gold")
    print("PART 2")
    print("Must contain %i bags" % bags_contained)


if __name__ == '__main__':
    main()
