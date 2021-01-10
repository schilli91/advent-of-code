def find_invalid_score(xmas_data):
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
