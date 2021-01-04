import pytest

from aoc2020.day_5.day_five import decode_boarding_pass, decode_row, decode_column


def test_decode_row():
    assert 70 == decode_row("BFFFBBFRRR")
    assert 14 == decode_row("FFFBBBFRRR")
    assert 102 == decode_row("BBFFBBFRLL")


def test_decode_column():
    assert 7 == decode_column("BFFFBBFRRR")
    assert 7 == decode_column("FFFBBBFRRR")
    assert 4 == decode_column("BBFFBBFRLL")


def test_decode_boarding_pass():
    assert 567 == decode_boarding_pass("BFFFBBFRRR")
    assert 119 == decode_boarding_pass("FFFBBBFRRR")
    assert 820 == decode_boarding_pass("BBFFBBFRLL")


if __name__ == '__main__':
    print("Day 5")
    pytest.main()
