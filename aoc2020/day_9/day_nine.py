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


if __name__ == '__main__':
    print("Day 9")
    first_invalid = find_invalid_score(XMAS_DATA)
    print(f"The first invalid score in the XMAS data is {first_invalid}.")
