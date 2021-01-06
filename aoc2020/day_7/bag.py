class Bag:

    def __init__(self, color, count=1):
        self.color = color
        self.count = count

    @classmethod
    def from_bag_string(cls, bag_string: str):
        return cls(bag_string.replace("bags", "").replace("bag", "").strip(), count=1)

    @classmethod
    def from_content_string(cls, content_string: str):
        # TODO: process no contents

        if "no other bag" in content_string:
            return []

        bag_strings = content_string.split(",")
        bag_strings = [b.replace("bags", "").replace("bag", "").strip() for b in bag_strings]

        bags = []
        for b in bag_strings:
            count, color = b.split(" ", maxsplit=1)
            bag = Bag(color, count=count)
            bags.append(bag)
        return bags
