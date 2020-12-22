from collections import defaultdict

from utils import parse_fname, read_input


def parse_input(input_str):
    return [int(a) for a in input_str.split('\n') if a != '']


def distribution_checksum(adapters, starting_jolts=0, final_jump=3):
    """Calculates the distribution of jolts across the path that uses all adapters
    and returns their checksum (the number of 1-jolt jumps multiplied by the number of
    3-jolt jumps)

    Args:
        - adapters (list(int)): the adapters to connect together
        - starting_jolts (int): the jolatage of the starting outlet
        - final_jump (int): the joltage jump to be made from the final adapter to the
            port

    Returns the checksum as an integer
    """
    adapters_c = adapters.copy()
    adapters_c.append(starting_jolts)
    adapters_c.sort()
    starting_idx = adapters_c.index(starting_jolts)
    adapters_c = adapters_c[starting_idx:]
    diffs = defaultdict(lambda: 0)
    for i in range(1, len(adapters_c)):
        diff = adapters_c[i] - adapters_c[i - 1]
        if diff < 1:
            continue
        elif diff > 4:
            break
        diffs[diff] += 1

    diffs[final_jump] += 1
    return diffs[1] * diffs[3]


def find_valid_paths(adapters, starting_jolts=0):
    """Finds all of the valid paths between an outlet with starting_jolts and the
    final adapter in a list of adapters

    Args:
        - adapters (list(int)): the adapters to connect together
        - starting_jolts (int): the jolatage of the starting outlet

    Returns the number of valid paths as an integer
    """
    adapters_c = adapters.copy()
    adapters_c.append(starting_jolts)
    adapters_c.sort()
    starting_idx = adapters_c.index(starting_jolts)
    adapters_c = adapters_c[starting_idx:]
    max_adapter = adapters_c.pop()
    adapter_paths = {}
    for a in adapters_c[::-1]:
        adapter_paths[a] = 0
        for i in range(1, 4):
            if a + i == max_adapter:
                adapter_paths[a] += 1
            elif a + i in adapter_paths.keys():
                adapter_paths[a] += adapter_paths[a + i]
    return adapter_paths[starting_jolts]


def main():
    input_str = read_input(*parse_fname(__file__))
    adapters = parse_input(input_str)

    checksum = distribution_checksum(adapters)
    print('PART 1')
    print('Distribution checksum: %i' % checksum)

    valid_paths = find_valid_paths(adapters)
    print('PART 2')
    print('All valid paths: %i' % valid_paths)


if __name__ == '__main__':
    main()
