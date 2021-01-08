import pytest

from aoc2020.day_7.bag import Bag
from aoc2020.day_7.day_seven import detect_outer_bags, detect_inner_bags

sample_rules = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""

more_sample_rules = """shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags."""

def test_detect_outer_bags():
    bag = Bag("shiny gold")
    assert 4 == len(detect_outer_bags(bag, sample_rules))


def test_detect_inner_bags():
    bag = Bag("shiny gold")
    assert 32 == detect_inner_bags(bag, sample_rules)
    assert 126 == detect_inner_bags(bag, more_sample_rules)


if __name__ == '__main__':
    print("Day 7")
    pytest.main()
