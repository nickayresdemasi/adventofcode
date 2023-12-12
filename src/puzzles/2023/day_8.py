"""Advent of Code 2023, Day 8"""

from collections import defaultdict
from itertools import cycle
from math import lcm
import re


def process_puzzle_input(puzzle_input: str) -> tuple[str, dict[str, list[str, str]]]:
    directions, nodes = puzzle_input.strip().split("\n\n")
    nodes = {
        re.findall(r"[A-Z]{3}", node)[0]: re.findall(r"[A-Z]{3}", node)[1:]
        for node in nodes.strip().split("\n")
    }
    return directions, nodes

def puzzle_solution_1(puzzle_input: str) -> int:
    directions, nodes = process_puzzle_input(puzzle_input)
    current_node = "AAA"
    steps = 0
    for d in cycle(directions):
        steps +=1
        current_node = nodes[current_node][0 if d == "L" else 1]
        if current_node == "ZZZ":
            break
    return steps


def puzzle_solution_2(puzzle_input: str) -> int:
    """Solves puzzle 2 by calculating # of steps each A node
    needs to reach a a Z node and finds the least common
    multiple among them. Assumes that paths are circular (ie.
    starting from same A or Z node will lead to same Z node)"""
    directions, nodes = process_puzzle_input(puzzle_input)
    a_nodes = [node for node in nodes if node.endswith("A")]
    steps_to_z = []
    for a_n in a_nodes:
        current_node = a_n
        steps = 0
        for d in cycle(directions):
            steps += 1
            next_node = nodes[current_node][0 if d == "L" else 1]
            if next_node.endswith("Z"):
                steps_to_z.append(steps)
                break
            current_node = next_node

    return lcm(*steps_to_z)


if __name__ == "__main__":
    ex_puzzle_input_1 = "\n".join([
        "LLR",
        "",
        "AAA = (BBB, BBB)",
        "BBB = (AAA, ZZZ)",
        "ZZZ = (ZZZ, ZZZ)"
    ])
    ex_puzzle_input_2 = "\n".join([
        "LR",
        "",
        "XXA = (XXB, XXX)",
        "XXB = (XXX, XXZ)",
        "XXZ = (XXB, XXX)",
        "YYA = (YYB, XXX)",
        "YYB = (YYC, YYC)",
        "YYC = (YYZ, YYZ)",
        "YYZ = (YYB, YYB)",
        "XXX = (XXX, XXX)"
    ])
    print("Puzzle #: Expected - Received")
    ps_1 = puzzle_solution_1(ex_puzzle_input_1)
    print(f"1: 6 - {ps_1}")
    ps_2 = puzzle_solution_2(ex_puzzle_input_2)
    print(f"2: 6 - {ps_2}")

