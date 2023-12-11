"""Advent of Code 2023, Day 5"""

from enum import Enum


def process_puzzle_input(puzzle_input: str) -> tuple[list[int], list[dict[str, list]]]:
    puzzle_input = puzzle_input.strip().split("\n\n")
    seeds = puzzle_input[0]
    mappings = puzzle_input[1:]
    seeds = [
        int(seed) for seed in
        seeds.split(":")[1].strip().split(" ")
    ]
    mapping_dicts = []
    for m in mappings:
        m = m.split("\n")
        m_cats = m[0].replace(" map:", "").split("-")
        m_src_cat, m_dst_cat = m_cats[0], m_cats[-1]
        m_ranges = [[int(n) for n in rng.strip().split(" ")] for rng in m[1:]]
        mapping_dicts.append(
            {"categories": [m_src_cat, m_dst_cat], "ranges": m_ranges}
        )

    return seeds, mapping_dicts


def puzzle_solution_1(puzzle_input: str) -> int:
    seeds, mappings = process_puzzle_input(puzzle_input)
    vals_by_cat = {"seed": seeds}

    for mapping in mappings:
        map_src_cat, map_dst_cat = mapping["categories"]
        map_rngs = mapping["ranges"]
        src_vals = vals_by_cat[map_src_cat]
        dst_vals = []
        for i, src_val in enumerate(src_vals):
            for map_rng in map_rngs:
                map_dst_start = map_rng[0]
                map_src_start = map_rng[1]
                map_rng_len = map_rng[2]
                if map_src_start <= src_val < map_src_start + map_rng_len:
                    dst_vals.append(map_dst_start + src_val - map_src_start)
                    break

            # map src val to itself if not found in any mapping ranges
            if len(dst_vals) < i + 1:
                dst_vals.append(src_val)
        vals_by_cat.update({map_dst_cat: dst_vals})

    return min(vals_by_cat["location"])


def puzzle_solution_2(puzzle_input: str) -> int:
    seeds, mappings = process_puzzle_input(puzzle_input)

    seed_ranges = [(seeds[i], seeds[i + 1]) for i in range(0, len(seeds), 2)]
    rngs_by_cat = {"seed": seed_ranges}

    for mapping in mappings:
        map_src_cat, map_dst_cat = mapping["categories"]
        map_rngs = mapping["ranges"]
        src_rngs = rngs_by_cat[map_src_cat]
        dst_rngs = []
        for src_rng in src_rngs:
            src_rng_start, src_rng_len = src_rng
            captured = False
            map_rng_idx = 0
            while not captured and map_rng_idx < len(map_rngs):
                # unpack mapping range
                map_dst_rng_start = map_rngs[map_rng_idx][0]
                map_src_rng_start = map_rngs[map_rng_idx][1]
                map_rng_len = map_rngs[map_rng_idx][2]

                src_rng_end = src_rng_start + src_rng_len
                map_src_rng_end = map_src_rng_start + map_rng_len
                dst_offset = map_dst_rng_start - map_src_rng_start

                # if ranges do not overlap, continue to next mapping range
                if src_rng_end <= map_src_rng_start or map_src_rng_end <= src_rng_start:
                    map_rng_idx += 1
                    continue

                left_leftover = max(map_src_rng_start - src_rng_start, 0)
                right_leftover = max(src_rng_end - map_src_rng_end, 0)

                if right_leftover > 0 and left_leftover > 0:
                    dst_rngs.append([map_dst_rng_start, map_rng_len])
                    src_rngs.append([map_src_rng_end, right_leftover])
                    src_rngs.append([src_rng_start, left_leftover])
                elif right_leftover > 0:
                    dst_rngs.append([src_rng_start + dst_offset, src_rng_len - right_leftover])
                    src_rngs.append([map_src_rng_end, right_leftover])
                elif left_leftover > 0:
                    dst_rngs.append([map_dst_rng_start, src_rng_len - left_leftover])
                    src_rngs.append([src_rng_start, left_leftover])
                else:
                    dst_rngs.append([src_rng_start + dst_offset, src_rng_len])

                captured = True

            # map range to itself if not covered by any mapping ranges
            if not captured:
                dst_rngs.append(src_rng)

        rngs_by_cat.update({map_dst_cat: dst_rngs})

    return min([l[0] for l in rngs_by_cat["location"]])


if __name__ == "__main__":
    puzzle_input = "\n".join([
        "seeds: 79 14 55 13",
        "",
        "seed-to-soil map:",
        "50 98 2",
        "52 50 48",
        "",
        "soil-to-fertilizer map:",
        "0 15 37",
        "37 52 2",
        "39 0 15",
        "",
        "fertilizer-to-water map:",
        "49 53 8",
        "0 11 42",
        "42 0 7",
        "57 7 4",
        "",
        "water-to-light map:",
        "88 18 7",
        "18 25 70",
        "",
        "light-to-temperature map:",
        "45 77 23",
        "81 45 19",
        "68 64 13",
        "",
        "temperature-to-humidity map:",
        "0 69 1",
        "1 0 69",
        "",
        "humidity-to-location map:",
        "60 56 37",
        "56 93 4"
    ])
    print("Puzzle #: Expected - Received")
    ps_1 = puzzle_solution_1(puzzle_input)
    print(f"1: 35 - {ps_1}")
    ps_2 = puzzle_solution_2(puzzle_input)
    print(f"2: 46 - {ps_2}")


