"""Advent of Code Day 1, 2023"""

import re


TRANSLATION_KEY = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}


def puzzle_solution_1(calibration_document):
    calibration_document = calibration_document.strip()
    checksum = 0
    for s in calibration_document.split("\n"):
        m = re.findall(r"\d", s)
        checksum += int(f"{m[0]}{m[-1]}")
    return checksum


def puzzle_solution_2(calibration_document):
    calibration_document = calibration_document.strip()
    mtch_pattern = rf"\d|{'|'.join(TRANSLATION_KEY.keys())}"
    rev_mtch_pattern = rf"\d|{'|'.join(TRANSLATION_KEY.keys())[::-1]}"
    checksum = 0
    for s in calibration_document.split("\n"):
        m_start = re.search(mtch_pattern, s).group()
        m_end = re.search(rev_mtch_pattern, s[::-1]).group()[::-1]
        d0 = TRANSLATION_KEY.get(m_end, m_end)
        d10 = TRANSLATION_KEY.get(m_start, m_start)
        checksum += int(f"{d10}{d0}")
    return checksum
