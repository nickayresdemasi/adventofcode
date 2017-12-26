def checksum(row):
    diff = max(row) - min(row)
    return diff


def checksum_2(row):
    row.sort(reverse=True)

    for i in range(len(row)):
        for j in range(len(row) - 1, i, -1):
            if row[j] > row[i] / 2:
                break
            elif row[i] % row[j] == 0:
                return row[i] // row[j]

    return 0


if __name__ == '__main__':
    file = open('day2.txt')
    text = file.read()
    spreadsheet = [[int(n) for n in row.split('\t')] for row in text.split('\n')]

    total_1 = 0
    total_2 = 0
    for row in spreadsheet:
        total_1 += checksum(row)
        total_2 += checksum_2(row)
    print(total_1)
    print(total_2)
