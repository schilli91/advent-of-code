import pytest

from aoc2020.day_6.day_six import count_custom_declaration

sample_customs_form = """abc

a
b
c

ab
ac

a
a
a
a

b"""


def test_custom_declaration():
    assert 11 == count_custom_declaration(sample_customs_form)


def test_custom_declaration_all_agree():
    assert 6 == count_custom_declaration(sample_customs_form, all_agree=True)


if __name__ == '__main__':
    print("Day 6")
    pytest.main()
