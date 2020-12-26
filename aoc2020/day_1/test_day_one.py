import pytest

sample_expense_report = [
    1721,
    979,
    366,
    299,
    675,
    1456,
]


def test_fix_expense_report():
    #res = fix_expense_report(sample_expense_report)
    res = 0
    assert 514579 == res

if __name__ == '__main__':
    print("Day 1")
    pytest.main()
