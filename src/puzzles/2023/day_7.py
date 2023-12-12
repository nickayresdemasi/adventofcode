"""Advent of Code 2023, Day 7"""

from collections import Counter, defaultdict
from operator import itemgetter


CARDS: list[str] = [
    "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"
]
CARDS_W_JOKERS: list[str] = [
    "J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"
]
HAND_TYPES: list[str] = [
    "High Card",
    "One Pair",
    "Two Pair",
    "3 of a Kind",
    "Full House",
    "4 of a Kind",
    "5 of a Kind"
]


def process_puzzle_input(puzzle_input: str) -> tuple[list[str], list[int]]:
    hands, bids = [], []
    for row in puzzle_input.strip().split("\n"):
        hands.append(row.split(" ")[0])
        bids.append(int(row.split(" ")[1]))
    return hands, bids


def score_hand(hand):
    hand_counter = Counter(hand)
    high_count = hand_counter.most_common(1)[0][1]
    uniq_cards = len(hand_counter.most_common())
    if high_count == 5:
        return "5 of a Kind"
    elif high_count == 4:
        return "4 of a Kind"
    elif high_count == 3 and uniq_cards == 2:
        return "Full House"
    elif high_count == 3:
        return "3 of a Kind"
    elif high_count == 2 and uniq_cards == 3:
        return "Two Pair"
    elif high_count == 2:
        return "One Pair"
    else:
        return "High Card"


def score_hand_w_joker(hand):
    hand_counter = Counter(hand)
    n_jokers = hand_counter["J"]
    if n_jokers == 5:
        high_count = 0
    else:
        high_count = max([c[1] for c in hand_counter.most_common() if c[0] != "J"])
    uniq_cards = len(hand_counter.most_common()) - min(n_jokers, 1)
    if high_count + n_jokers == 5:
        return "5 of a Kind"
    elif high_count + n_jokers == 4:
        return "4 of a Kind"
    elif high_count + n_jokers == 3 and uniq_cards == 2:
        return "Full House"
    elif high_count + n_jokers == 3:
        return "3 of a Kind"
    elif high_count + n_jokers == 2 and uniq_cards == 3:
        return "Two Pair"
    elif high_count + n_jokers == 2:
        return "One Pair"
    else:
        return "High Card"


def puzzle_solution_1(puzzle_input: str) -> int:
    hands, bids = process_puzzle_input(puzzle_input)
    hands_by_score = defaultdict(list)
    for hand in hands:
        hands_by_score[score_hand(hand)].append(hand)
    ranked_hands = []
    for ht in HAND_TYPES:
        for i in range(4, -1, -1):
            hands_by_score[ht].sort(key=lambda h: CARDS.index(h[i]))
        ranked_hands.extend(hands_by_score[ht])
    checksum = sum([(rank + 1) * bids[hands.index(hand)] for rank, hand in enumerate(ranked_hands)])
    return checksum


def puzzle_solution_2(puzzle_input: str) -> int:
    hands, bids = process_puzzle_input(puzzle_input)
    hands_by_score = defaultdict(list)
    for hand in hands:
        hands_by_score[score_hand_w_joker(hand)].append(hand)
    ranked_hands = []
    for ht in HAND_TYPES:
        for i in range(4, -1, -1):
            hands_by_score[ht].sort(key=lambda h: CARDS_W_JOKERS.index(h[i]))
        ranked_hands.extend(hands_by_score[ht])
    checksum = sum([(rank + 1) * bids[hands.index(hand)] for rank, hand in enumerate(ranked_hands)])
    return checksum


if __name__ == "__main__":
    ex_puzzle_input = "\n".join([
        "32T3K 765",
        "T55J5 684",
        "KK677 28",
        "KTJJT 220",
        "QQQJA 483"
    ])
    print("Puzzle #: Expected - Received")
    ps_1 = puzzle_solution_1(ex_puzzle_input)
    print(f"1: 6440 - {ps_1}")
    ps_2 = puzzle_solution_2(ex_puzzle_input)
    print(f"2: 5905 - {ps_2}")


