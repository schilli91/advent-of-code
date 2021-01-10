from typing import List

from aoc2020.day_8.boot_code import BOOT_CODE
from aoc2020.day_8.instruction import Instruction


def run_boot_code(boot_code) -> int:
    instructions = _parse_boot_code(boot_code)
    return _run_instructions(instructions)


def _parse_boot_code(boot_code: str) -> List[Instruction]:
    return [Instruction.from_code_line(line) for line in boot_code.splitlines()]


def _run_instructions(instructions: List[Instruction]):
    index = 0
    accumulator = 0
    visited = []
    current = instructions[index]
    while current not in visited:
        visited.append(current)
        if current.operator == "nop":
            index = index + 1
        elif current.operator == "acc":
            accumulator = accumulator + current.argument
            index = index + 1
        elif current.operator == "jmp":
            index = index + current.argument

        current = instructions[index]
    return accumulator


def fix_boot_code(boot_code):
    instructions = _parse_boot_code(boot_code)
    index = 0
    accumulator = 0
    visited = set()
    # start = [index, accumulator]
    # start_visited = []
    fixed = False
    fixed_instructions = []

    current = instructions[index]
    interrupted = False
    while not interrupted:

        # # break on success
        # if index == len(instructions):
        #     return accumulator
        #
        # # break on out of bounds
        # if index < 0 or index > len(instructions):
        #     index, accumulator = (0, 0)
        #     visited = set()
        #     fixed = False
        #     current = instructions[index]

        # break on visited
        if current in visited:
            index, accumulator = (0, 0)
            visited = set()
            fixed = False
            current = instructions[index]

        if current.operator == "nop":
            if not fixed and current not in fixed_instructions:
                # print(f"fix ({current.operator} {current.argument}) -> (jmp {current.argument})")
                fixed = True
                fixed_instructions.append(current)
                _do_jmp(current, index)
            else:
                index = _do_nop(index)

        elif current.operator == "acc":
            accumulator, index = _do_acc(accumulator, current, index)

        elif current.operator == "jmp":
            if not fixed and current not in fixed_instructions:
                # print(f"fix ({current.operator} {current.argument}) -> (nop {current.argument})")
                fixed = True
                fixed_instructions.append(current)
                index = _do_nop(index)
            else:
                index = _do_jmp(current, index)

        visited.add(current)

        # break on success
        if index == len(instructions):
            return accumulator

        # break on out of bounds
        if index < 0 or index > len(instructions):
            index, accumulator = (0, 0)
            visited = set()
            fixed = False
        current = instructions[index]
    return False


def _do_nop(index):
    index = index + 1
    return index


def _do_acc(accumulator, current, index):
    accumulator = accumulator + current.argument
    index = index + 1
    return accumulator, index


def _do_jmp(current, index):
    index = index + current.argument
    return index


if __name__ == '__main__':
    print("Day 8")
    accumulator = run_boot_code(BOOT_CODE)
    print(f"The accumulator has value {accumulator} immediately before any instruction is"
          f" executed a second time.")

    accumulator = fix_boot_code(BOOT_CODE)
    print(f"The accumulator has value {accumulator} when the program terminates.")
