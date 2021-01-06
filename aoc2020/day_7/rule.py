from typing import List

from aoc2020.day_7.bag import Bag


class Rule:
    bag: Bag = None
    content: List[Bag] = []

    def __init__(self, rule_str: str):
        _bag, _content = rule_str.split("contain")
        _bag, _content = _bag.strip(), _content.strip().replace(".", "")
        self.bag = Bag.from_bag_string(_bag)
        self.content = Bag.from_content_string(_content)


if __name__ == '__main__':
    rule = Rule("light red bags contain 1 bright white bag, 2 muted yellow bags.")
    print(rule)
