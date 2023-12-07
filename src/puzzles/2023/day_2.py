"""Advent of Code Day 2, 2023"""


import re


def find_max_draw(game, color):
    draws = [
        int(m[0]) for m in
        re.findall(rf"(\d+) ({color})", game)
    ]
    return max(draws)


def puzzle_solution_1(games):
    # process input
    games = games.strip().split("\n")

    # set game parameters
    n_red_cubes = 12
    n_green_cubes = 13
    n_blue_cubes = 14

    # calculate checksum
    checksum = 0
    for i, game in enumerate(games):
        if find_max_draw(game, "red") > n_red_cubes:
            continue
        if find_max_draw(game, "green") > n_green_cubes:
            continue
        if find_max_draw(game, "blue") > n_blue_cubes:
            continue
        checksum += i + 1  # add 1 to i to reflect game #

    return checksum


def puzzle_solution_2(games):
    # process input
    games = games.strip().split("\n")

    # calculate checksum
    checksum = 0
    for game in games:
        game_power = (
            find_max_draw(game, "red")
            * find_max_draw(game, "green")
            * find_max_draw(game, "blue")
        )
        checksum += game_power

    return checksum
