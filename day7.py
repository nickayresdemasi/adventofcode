import re
import sys


def create_map(mapping):
    discs = {}
    weights = {}
    for m in mapping:
        weight = int(re.search(r"[0-9]+", m).group(0).strip())
        try:
            k, v = m.split('->')
        except:
            key = re.sub(r"\(\d+\)", "", m).strip()
            weights[key] = weight
        else:
            key = re.sub(r"\(\d+\)", "", k).strip()
            values = [value.strip() for value in v.split(',')]
            weights[key] = weight
            discs[key] = values

    return discs, weights


def find_disc(key, discs, weights):
    total_ws = []
    for v in discs[key]:
        if v in discs.keys():
            total_ws.append(find_disc(v, discs, weights) + weights[v])
        else:
            total_ws.append(weights[v])

    if len(total_ws) != set(total_ws):
        diff = max(total_ws) - min(total_ws)
        if total_ws.count(max(total_ws)) == 1:
            diff = -diff
        for i in range(len(total_ws)):
            if total_ws.count(total_ws[i]) == 1:
                print(weights[discs[key][i]] + diff)
                sys.exit()

    disc_weight = max(total_ws) * len(total_ws)
    return disc_weight


if __name__ == '__main__':
    file = open('day7.txt', 'r')
    text = file.read()
    mapping = [r for r in text.split('\n')]

    discs, weights = create_map(mapping)
    find_disc('eugwuhl', discs, weights)
