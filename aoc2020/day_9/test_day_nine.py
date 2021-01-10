import pytest

from aoc2020.day_9.day_nine import find_invalid_score, validate_score, find_weakness

sample_xmas_data = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576"""


def test_find_invalid_score():
    assert 127 == find_invalid_score(sample_xmas_data, 5)


def test_validate_score():
    preamble = [i + 1 for i in range(25)]
    assert True == validate_score(preamble, 26)
    assert True == validate_score(preamble, 49)

    assert False == validate_score(preamble, 100)
    assert False == validate_score(preamble, 50)

    preamble[19] = 45
    assert True == validate_score(preamble, 26)
    assert True == validate_score(preamble, 64)
    assert True == validate_score(preamble, 66)

    assert False == validate_score(preamble, 65)


def test_find_weakness():
    assert 62 == find_weakness(sample_xmas_data, 127)


if __name__ == '__main__':
    print("Day 9")
    pytest.main()
