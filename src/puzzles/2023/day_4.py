"""Advent of Code 2023 - Day 4"""

from collections import Counter
from typing import List


def process_puzzle_input(puzzle_input: str) -> List[List[List[int]]]:
    """Transform puzzle input into a three dimensional matrix:

    1st dimension - card
    2nd dimension - number categories (winning & play)
    3rd dimension - numbers"""
    cards = []
    for row in puzzle_input.strip().split("\n"):
        # winning nums: nums that result in points
        # play nums: nums that can match winning nums
        winning_nums, play_nums = row.split(":")[1].split("|")

        # convert numbers from strings to ints
        winning_nums = [num for num in winning_nums.strip().split(" ") if num]
        play_nums = [num for num in play_nums.strip().split(" ") if num]

        cards.append([winning_nums, play_nums])
    return cards


def puzzle_solution_1(puzzle_input: str) -> int:
    cards = process_puzzle_input(puzzle_input)
    points = 0
    for i, card in enumerate(cards):
        winning_nums, play_nums = card

        # determine how many play nums match winning nums
        matching_nums = [num for num in play_nums if num in winning_nums]

        # no points if no matching nums
        if matching_nums:
            points += 2 ** (len(matching_nums) - 1)
    return points


def puzzle_solution_2(puzzle_input: str) -> int:
    cards = process_puzzle_input(puzzle_input)

    # keep track of number of matching nums per card
    card_outcomes = []
    for card in cards:
        winning_nums, play_nums = card
        matching_nums = len([num for num in play_nums if num in winning_nums])
        card_outcomes.append(matching_nums)

    # determine number of duplicates created by each card
    card_counter = Counter()
    for card_num, matching_nums in enumerate(card_outcomes):
        card_counter[card_num] += 1
        for i in range(card_num, card_num + matching_nums):
            card_counter[i + 1] += card_counter[card_num]

    # calculate total cards awarded
    total_cards = card_counter.total()
    return total_cards


if __name__ == "__main__":
    puzzle_input = "\n".join(
        [
            "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
            "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
            "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
            "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
            "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
            "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11",
        ]
    )
    ps_1 = puzzle_solution_1(puzzle_input)
    ps_2 = puzzle_solution_2(puzzle_input)
    print("Puzzle #: Expected - Received")
    print(f"1: 13 - {ps_1}")
    print(f"2: 30 - {ps_2}")
