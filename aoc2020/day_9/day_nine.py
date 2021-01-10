from aoc2020.day_9.xmas_data import XMAS_DATA


def find_invalid_score(xmas_data: str, preamble_length: int = 25):
    xmas_data_values = [int(i) for i in xmas_data.splitlines()]
    preamble = xmas_data_values[:preamble_length]

    for score in xmas_data_values[preamble_length:]:
        if not validate_score(preamble, score):
            return score
        preamble = preamble[1:]
        preamble.append(score)

    return False


def validate_score(preamble, score):
    valid_scores = set()
    for i in preamble:
        for j in preamble:
            if i != j:
                valid_scores.add(i + j)

    return score in valid_scores


def find_weakness(xmas_data, first_invalid):
    xmas_data_values = [int(i) for i in xmas_data.splitlines() if int(i) < first_invalid]

    res = _find_weakness(xmas_data_values, 0, first_invalid)
    if res != False:
        return min(res) + max(res)

    return False


def _find_weakness(values, start_index, target_sum):
    candidates = []
    for i in range(start_index, len(values)):
        candidates.append(values[i])

        if sum(candidates) == target_sum:
            return candidates

        if sum(candidates) > target_sum:
            return _find_weakness(values, start_index + 1, target_sum)
    return False


if __name__ == '__main__':
    print("Day 9")
    first_invalid = find_invalid_score(XMAS_DATA)
    print(f"The first invalid score in the XMAS data is {first_invalid}.")

    encryption_weakness = find_weakness(XMAS_DATA, 552655238)
    print(f"The encryption weakness of the XMAS data is {encryption_weakness}.")
