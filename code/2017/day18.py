'''
@author: Nick DeMasi

Code to complete Day 18 of 2017 Advent of
Code using Python 3

'''


import os
import string

from register import Register


ABS_PATH = 'C://Users/ldema/Coding/python_projects/adventofcode2017'


def duet(instructions):
    '''Plays through instructions in Duet code'''

    # instantiate SoundRegister object
    sr1 = SoundRegister(0, string.ascii_lowercase)
    sr2 = SoundRegister(1, string.ascii_lowercase)

    # instantiate tracking variables
    rs = [sr1, sr2]
    counter = [0, 0]
    i = 0
    moves = 0

    # iterate through instructions
    while True:
        # split out instruction into components
        temp = instructions[counter[i]].split(' ')

        # convert numerical components to integers
        i_list = [x if x.isalpha() else int(x) for x in temp]

        # insert value into other Sound Register's queue attribute
        if i_list[0] == 'snd':
            if i == 1:
                moves += 1
            rs[i].send(i_list[1], rs[abs(i - 1)].queue)

            # indicate that other Sound Register can now accept values
            rs[abs(i -1)].flag = '+'
            counter[i] += 1
        # set values in current register
        elif i_list[0] == 'set':
            rs[i].set(i_list[1], i_list[2])
            counter[i] += 1
        # add values in current register
        elif i_list[0] == 'add':
            rs[i].add(i_list[1], i_list[2])
            counter[i] += 1
        # multiply values in current register
        elif i_list[0] == 'mul':
            rs[i].mul(i_list[1], i_list[2])
            counter[i] += 1
        # modulo values in current register
        elif i_list[0] == 'mod':
            rs[i].mod(i_list[1], i_list[2])
            counter[i] += 1

        # recieve values from SoundRegister's queue
        elif i_list[0] == 'rcv':
            # if queue exists set values
            if rs[i].queue:
                rs[i].recieve(i_list[1])
                counter[i] += 1
            # otherwise terminate processes and switch to other SoundRegister
            # DO NOT MOVE ON TO NEXT INSTRUCTION
            else:
                rs[i].flag = '-'
                i = abs(i - 1)

        # jump if x is non-zero
        elif i_list[0] == 'jgz':
            if rs[i].get_value(i_list[1]) > 0:
                counter[i] += rs[i].get_value(i_list[2])
            else:
                counter[i] += 1

        # if both SoundRegister flags indicate termination, stop duet and return answer
        if sr1.flag == '-' and sr2.flag == '-':
            print("Part 2:             %d" % moves)
            return


class SoundRegister(Register):
    def __init__(self, val, s):
        super().__init__(val, s)
        self.queue = []
        self.flag = 'neutral'

    def play(self, sound):
        '''Plays a sound and stores it'''
        self.last_played = self.get_value(sound)

    def recieve(self, x):
        '''Sets value at position x of register to oldest queue item'''
        self.register[x] = self.queue.pop()

    def recover(self, x):
        '''Recovers and returns the value of the most recently played sound
        if x > 0'''
        if self.get_value(x) > 0:
            return self.last_played
        else:
            return None

    def send(self, x, dest):
        '''Sends a value x to a desitination list'''
        dest.insert(0, self.get_value(x))


if __name__ == '__main__':
    # read in instructions
    path = os.path.join(ABS_PATH, 'input/day18.txt')
    file = open(path, 'r')
    instructions = file.read().split('\n')

    # initiate duet program for part 1
    duet(instructions)
