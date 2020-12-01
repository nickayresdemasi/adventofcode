'''
@author: Nick DeMasi

Code to complete Day 23 of 2017 Advent of
Code using Python 3

'''

A = 1
B = 2
C = 3
D = 4
E = 5
F = 6

def turing_machine(steps):
    '''Runs a Turing Machine for a certain number of steps, returns
    a checksum'''

    # create tracking variables
    pos = 0
    state = A
    tape = {0: 0}

    # iterate through steps
    for i in range(steps):
        if tape[pos] == 0:
            if state == A:
                tape[pos] = 1
                pos += 1
                state = B
            elif state == B:
                tape[pos] = 1
                pos -= 1
                state = C
            elif state == C:
                tape[pos] = 1
                pos += 1
                state = E
            elif state == D:
                tape[pos] = 1
                pos -= 1
                state = A
            elif state == E:
                pos += 1
                state = A
            else:
                tape[pos] = 1
                pos += 1
                state = E
        else:
            if state == A:
                tape[pos] = 0
                pos -= 1
                state = B
            elif state = B:
                tape[pos] = 0
                pos += 1
                state = E
            elif state == C:
                tape[pos] = 0
                pos -= 1
                state = D
            elif state == D:
                pos -= 1
                state = A
            elif state == E:
                tape[pos] = 0
                pos += 1
                state = F
            else:
                pos += 1
                state = A

        # update tape
        if pos not in tape.keys():
            tape[pos] = 0

    # calculate and return a checksum
    return sum(list(tape.values()))

if __name__ == '__main__':
    # instantiate TuringMaching
    print("Part 1:          %d" % turing_machine(12683008))
