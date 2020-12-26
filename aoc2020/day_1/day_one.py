from aoc2020.day_1.expense_report import expense_report


def fix_expense_report(expense_report, num_summand):
    if num_summand == 2:
        return fix_expense_report_two_summands(expense_report)

    if num_summand == 3:
        return fix_expense_report_three_summands(expense_report)


def fix_expense_report_two_summands(expense_report):
    for i in expense_report:
        for j in expense_report:
            if (i + j == 2020):
                return i * j

    return False


def fix_expense_report_three_summands(expense_report):
    for i in expense_report:
        for j in expense_report:
            for k in expense_report:
                if i == j or i == j or j == k:
                    continue
                if (i + j + k == 2020):
                    return i * j * k

    return False


if __name__ == '__main__':
    print("Day 1")
    res = fix_expense_report(expense_report, 2)
    print(f"The expense report result with two summands is {res}.")
    res = fix_expense_report(expense_report, 3)
    print(f"The expense report result with three summands is {res}.")
