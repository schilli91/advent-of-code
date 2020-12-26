LOWER_BOUND = 240920
UPPER_BOUND = 789857


def get_possible_candidates_part_one():
    candidates = []
    for candidate in range(LOWER_BOUND, UPPER_BOUND):
        candidate = str(candidate)
        if not _complies_never_decrease(candidate):
            continue
        if not _complies_double_value(candidate):
            continue
        candidates.append(candidate)

    return candidates


def get_possible_candidates_part_two():
    candidates = []
    for candidate in range(LOWER_BOUND, UPPER_BOUND):
        candidate = str(candidate)
        if not _complies_never_decrease(candidate):
            continue
        if not _complies_double_value(candidate):
            continue
        if not _complies_true_double(candidate):
            continue
        candidates.append(candidate)

    return candidates


def _complies_never_decrease(number_string):
    current = number_string[0]
    for digit in number_string:
        if digit < current:
            return False
        current = digit
    return True


def _complies_double_value(number_string):
    if len(set(number_string)) >= 6:
        return False
    # TODO: check whether there are actual doubles? => Not necessary, since the numbers never decrease.
    return True


def _complies_true_double(number_string):
    amounts_of_numbers = _count_numbers(number_string)
    _ = 0
    for _, amount in amounts_of_numbers.items():
        if amount == 2:
            return True

    return False


def _count_numbers(number_string):
    amount_of_numbers = {}
    for digit in number_string:
        if digit not in amount_of_numbers:
            amount_of_numbers[digit] = 1
        else:
            amount_of_numbers[digit] += 1
    return amount_of_numbers


if __name__ == '__main__':
    print('Day 3\n')

    print('1️⃣ Part One')
    candidates = get_possible_candidates_part_one()
    print('Possible candidates:')
    for candidate in candidates:
        print(candidate)

    print('\nNumber of candidates: {}.'.format(len(candidates)))
    # 1167
    # 1154

    # print('Running test samples.\n')

    print('\n===============================================================\n')

    print('2️⃣ Part Two')

    candidates = get_possible_candidates_part_two()
    # print('Possible candidates:')
    # for candidate in candidates:
    #    print(candidate)

    print('\nNumber of candidates: {}.'.format(len(candidates)))
