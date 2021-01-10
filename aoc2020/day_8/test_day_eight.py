import pytest

from aoc2020.day_8.day_eight import run_boot_code, fix_boot_code

sample_boot_code = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""


def test_run_boot_code():
    assert 5 == run_boot_code(sample_boot_code)

def test_fix_boot_code():
    assert 8 == fix_boot_code(sample_boot_code)

if __name__ == '__main__':
    print("Day 8")
    pytest.main()
