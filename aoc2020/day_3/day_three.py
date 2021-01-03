from functools import reduce

from aoc2020.day_3.toboggan_map import toboggan_map


def traverse_map(map: str, slope=(3, 1)):
    lines = map.splitlines()
    step = 0
    position = 0
    trees = 0
    for line in lines:
        if (step % slope[1]) != 0:
            step = step + 1
            continue
        if line[position] == "#":
            trees = trees + 1
        position = (position + slope[0]) % len(line)
        step = step + 1

    return trees


def traverse_map_multi_slopes(map: str, slopes: list):
    num_trees = []
    for slope in slopes:
        num_trees.append(traverse_map(map, slope))
    return reduce(lambda x, y: x * y, num_trees)


if __name__ == '__main__':
    print("Day 3")
    slope = (3, 1)
    trees = traverse_map(toboggan_map, slope)
    print(f"With slope {slope}, we would cross {trees} trees.")

    slopes = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2),
    ]
    trees = traverse_map_multi_slopes(toboggan_map, slopes)
    print(f"With following slopes, the product of all {trees} trees crossed is.")
    print(f"slopes: {slopes}")
