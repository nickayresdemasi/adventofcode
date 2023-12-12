from collections import defaultdict

from utils import parse_fname, read_input


def parse_input(input_str):
    return [int(s) for s in input_str.split('\n') if s != '']


class EncodingError(object):
    """Contains methods for decrypting a cypher consisting of a list of ints"""
    def __init__(self, cypher, preamble_length):
        """Initializes an EncodingError object

        Args:
            - cypher (list(int)): list of integers in cypher
            - preamble_length (int): the number of integers (taken from the
                start of the cypher) that make up the cypher's preamble

        Returns an EncoddingError object
        """
        self.cypher = cypher
        self.preamble = cypher[:preamble_length].copy()
        self.preamble_length = preamble_length

        self.sumlib = None

    def find_faulty_sum(self):
        """ Finds the first number in the cypher which is not equal to the sum
        of two of the preamble_length numbers that come before it

        Returns the faulty sum as an int if one exists, otherwise None
        """
        if self.sumlib is None:
            raise ValueError('sumlib must be generated before running this function')

        preamble_c = self.preamble.copy()
        sumlib_c = self.sumlib.copy()
        for i, datum in enumerate(self.cypher[self.preamble_length:]):
            valid_sums = [k for k in sumlib_c.keys() if len(sumlib_c[k]) > 0]
            if datum not in valid_sums:
                return datum
            idx_0 = preamble_c.pop(0)

            # update sumlib
            for k, v in sumlib_c.items():
                sumlib_c[k] = [pair for pair in v if idx_0 not in pair]
            for idx in preamble_c:
                sumlib_c[datum + idx].append((datum, idx))

            # add datum to preamble
            preamble_c.append(datum)

        return None

    def find_contiguous_series_checksum(self, target_sum):
        """Finds a contiguous series of integers in the cypher that add up to the
        target_sum and computes their cheecksum (the sum of the min and max integers
        in the series)

        Args:
            - target_sum (int): number to which series must sum up to

        Returns the checksom as an int if a series exists, otherwise None
        """
        target_idx = self.cypher.index(target_sum)
        counter = 0
        combo = []
        while counter < len(self.cypher):
            if counter == target_idx:
                combo = []
                counter += 1
            elif sum(combo) < target_sum:
                combo.append(self.cypher[counter])
                counter += 1
            elif sum(combo) > target_sum:
                del combo[0]
            else:
                return min(combo) + max(combo)

        return None

    def generate_sumlib_from_preamble(self):
        sumlib = defaultdict(list)
        preamble_c = self.preamble.copy()
        for _ in range(len(preamble_c) - 1):
            v1 = preamble_c.pop(0)
            for v2 in preamble_c:
                sumlib[v1 + v2].append((v1, v2))
        self.sumlib = sumlib


def main():
    input_str = read_input(*parse_fname(__file__))
    code = parse_input(input_str)

    ee = EncodingError(code, preamble_length=25)
    ee.generate_sumlib_from_preamble()

    faulty_sum = ee.find_faulty_sum()
    print('PART 1')
    if faulty_sum is None:
        print('No faulty sum found')
    else:
        print('Faulty sum %i found' % faulty_sum)

    checksum = ee.find_contiguous_series_checksum(faulty_sum)
    print('PART 1')
    if checksum is None:
        print('No contiguous combo found')
    else:
        print('Contiguous combo checksum: %i' % checksum)


if __name__ == '__main__':
    main()
