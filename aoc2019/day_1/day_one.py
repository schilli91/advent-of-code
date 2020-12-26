puzzle_input = [
    80228,
    76027,
    101696,
    66033,
    127249,
    104564,
    88957,
    82536,
    131331,
    62571,
    129935,
    138764,
    122011,
    82908,
    83358,
    56584,
    85483,
    110398,
    87103,
    145728,
    87305,
    116387,
    145243,
    118656,
    92624,
    86152,
    81056,
    98776,
    109949,
    126863,
    131046,
    134570,
    97818,
    123881,
    105902,
    60102,
    100226,
    101041,
    70950,
    110903,
    71779,
    80531,
    144679,
    100346,
    130079,
    55606,
    92984,
    136022,
    126633,
    77104,
    118037,
    148426,
    62327,
    56250,
    133496,
    69308,
    125495,
    122131,
    56864,
    127532,
    94194,
    64268,
    80166,
    83250,
    96506,
    87668,
    142137,
    142915,
    148287,
    109471,
    79349,
    148270,
    104627,
    109657,
    86225,
    111411,
    144666,
    91402,
    140834,
    138587,
    117809,
    114288,
    126467,
    100089,
    78745,
    92180,
    89969,
    128868,
    128085,
    129931,
    64047,
    71968,
    111512,
    143771,
    149658,
    146102,
    52655,
    130193,
    109013,
    120465,
]


def part_one():
    fuel_requirements = 0

    for module in puzzle_input:
        module_fuel = int(module / 3) - 2
        print(module_fuel)
        fuel_requirements = fuel_requirements + module_fuel

    print(fuel_requirements)


def get_fuel_requirements():
    fuel_requirements = 0
    for module in puzzle_input:
        fuel_requirements += _get_module_fuel(module)
    return fuel_requirements

def _get_module_fuel(weight):
    sum = 0
    module_fuel = int(weight / 3) - 2
    sum += module_fuel if module_fuel > 0 else 0
    if module_fuel <= 0:
        return sum
    return sum + _get_module_fuel(module_fuel)


def test_get_module_fuel():
    puzzle_input = [12, 14, 1969, 100756, ]

    print(_get_module_fuel(12))
    assert _get_module_fuel(12) == 2

    print(_get_module_fuel(1969))
    assert _get_module_fuel(1969) == 966

    print(_get_module_fuel(100756))
    assert _get_module_fuel(100756) == 50346


# puzzle_input = [12, 14, 1969, 100756, ]
if __name__ == '__main__':
    # part_one()
    # test_get_module_fuel()
    print('Complete fuel requirements: {}'.format(get_fuel_requirements()))
