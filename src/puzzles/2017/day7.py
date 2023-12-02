'''
@author: Nick DeMasi

Code to complete Day 7 of 2017 Advent of
Code using Python 3

'''

import os
import re
import sys


ABS_PATH = 'C://Users/ldema/Coding/python_projects/adventofcode2017'


class DiscTower(object):
    def __init__(self):
        self.discs = {}
        self.weights = {}

    def create_map(self, mapping):
        for m in mapping:
            weight = int(re.search(r"[0-9]+", m).group(0).strip())
            if '->' in m:
                k, v = m.split('->')
                key = re.sub(r"\(\d+\)", "", k).strip()
                values = [value.strip() for value in v.split(',')]
                self.weights[key] = weight
                self.discs[key] = values
            else:
                key = re.sub(r"\(\d+\)", "", m).strip()
                self.weights[key] = weight

    def find_origin(self):
        values = []
        for v in self.discs.values():
            values += v

        for k in self.discs.keys():
            if k in values:
                continue
            else:
                return k

        return False

    def find_imbalance(self, key):
        total_ws = []
        for v in self.discs[key]:
            if v in self.discs.keys():
                total_ws.append(self.find_imbalance(v) + self.weights[v])
            else:
                total_ws.append(self.weights[v])

        if len(total_ws) != set(total_ws):
            diff = max(total_ws) - min(total_ws)
            if total_ws.count(max(total_ws)) == 1:
                diff = -diff
            for i in range(len(total_ws)):
                if total_ws.count(total_ws[i]) == 1:
                    imbalance = self.weights[self.discs[key][i]] + diff
                    print("Part 2:        ", imbalance)
                    sys.exit()

        disc_weight = max(total_ws) * len(total_ws)
        return disc_weight


if __name__ == '__main__':
    path = os.path.join(ABS_PATH, 'input/day7.txt')
    file = open(path, 'r')
    text = file.read()
    mapping = [r for r in text.split('\n')]

    dt = DiscTower()
    dt.create_map(mapping)
    origin = dt.find_origin()
    print("Part 1:        ", origin)
    dt.find_imbalance(origin)
