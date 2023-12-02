'''
@author: Nick DeMasi

Code to complete Day 4 of 2017 Advent of
Code using Python 3

'''

import os


ABS_PATH = 'C://Users/ldema/Coding/python_projects/adventofcode2017'


def duplicates(passphrase):
    '''Searches for duplicate strings in line of text'''
    passphrase_list = passphrase.split(" ")
    if len(passphrase_list) != len(set(passphrase_list)):
        return True
    return False


def palindromes(passphrase):
    '''Searches for palindromes in line of text'''
    p_list = passphrase.split(" ")
    sorted_words = []
    for word in p_list:
        sorted_words.append(''.join(sorted(word)))

    if len(sorted_words) != len(set(sorted_words)):
        return True
    return False


if __name__ == '__main__':
    path = os.path.join(ABS_PATH, 'input/day4.txt')
    file = open(path, 'r')
    text = file.read()

    non_dup = 0
    non_pal = 0
    for passphrase in text.split('\n'):
        if not duplicates(passphrase):
            non_dup += 1
        if not palindromes(passphrase):
            non_pal += 1

    print("Part 1:        ", non_dup)
    print("Part 2:        ", non_pal)
