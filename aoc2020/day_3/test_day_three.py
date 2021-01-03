import pytest

from aoc2020.day_3.day_three import traverse_map, traverse_map_multi_slopes

sample_map = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#"""


def test_traverse_map():
    res = traverse_map(sample_map, (3, 1))
    assert 7 == res


def test_traverse_map_multi_slopes():
    slopes = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2),
    ]
    res = traverse_map_multi_slopes(sample_map, slopes)
    assert 336 == res


if __name__ == '__main__':
    print("Day 3")
    pytest.main()
