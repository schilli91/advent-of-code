from aoc2020.day_7.bag import Bag
from aoc2020.day_7.rule import Rule
from aoc2020.day_7.rule_set import RULES_SET


def detect_outer_bags(bag: Bag, rules_str: str):
    rules = _parse_rules_str(rules_str)
    outer_bags = set()
    outer_bags.update(_find_outer_bags(bag, rules))
    num_outer_bags = 0

    while num_outer_bags < len(outer_bags):
        num_outer_bags = len(outer_bags)
        new_outer_bags = set()

        for bag in outer_bags:
            new_outer_bags.update(_find_outer_bags(bag, rules))

        outer_bags.update(new_outer_bags)
    return outer_bags


def _find_outer_bags(bag: Bag, rules):
    outer_bags = []
    for color, rule in rules.items():
        for b in rule.content:
            if b.color == bag.color:
                outer_bags.append(rule.bag)
    return outer_bags


def _parse_rules_str(rules_str: str):
    rules = {}
    for line in rules_str.splitlines():
        rule = Rule(line)
        rules[rule.bag.color] = rule
    return rules

def detect_inner_bags(bag: Bag, rules_str: str):
    return False

if __name__ == '__main__':
    print("Day 7")
    bag = Bag("shiny gold")
    outer_bags = detect_outer_bags(bag, RULES_SET)
    print(f"A {bag.color} bag can be contained in {len(outer_bags)} bags.")
