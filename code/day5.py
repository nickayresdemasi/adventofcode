def exit_array(l):
    pos = 0
    moves = 0
    while pos < len(l):
        jump = l[pos]
        if jump >= 3:
            l[pos] -= 1
        else:
            l[pos] += 1
        pos += jump
        moves += 1

    return moves


if __name__ == '__main__':
    file = open('day5.txt', 'r')
    text = file.read()
    nums = [int(n) for n in text.split('\n')]
    print(exit_array(nums))
