import pytest

from aoc2020.day_1.day_one import fix_expense_report

sample_expense_report = [
    1721,
    979,
    366,
    299,
    675,
    1456,
]


def test_fix_expense_report():
    res = fix_expense_report(sample_expense_report, 2)
    assert 514579 == res
    res = fix_expense_report(sample_expense_report, 3)
    assert 241861950 == res


if __name__ == '__main__':
    print("Day 1")
    pytest.main()
