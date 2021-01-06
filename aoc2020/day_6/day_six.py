from functools import reduce

from aoc2020.day_6.customs_form import CUSTOMS_FORM


def count_custom_declaration(customs_form: str, all_agree=False):
    groups = customs_form.split("\n\n")
    groups_questions = []

    count_mechanism = _count_questions_all_agree if all_agree else _count_questions_of_group

    for group in groups:
        groups_questions.append(count_mechanism(group))
    return reduce(lambda x, y: x + y, groups_questions)


def _count_questions_of_group(group):
    group_questions = set()
    for person in group.splitlines():
        group_questions.update([question for question in person])
    return len(group_questions)


def _count_questions_all_agree(group):
    person_sets = []
    for person in group.splitlines():
        person_sets.append({question for question in person})

    group_questions = reduce(lambda a, b: a.intersection(b), person_sets)

    return len(group_questions)


if __name__ == '__main__':
    print("Day 6")
    num_custom_declarations = count_custom_declaration(CUSTOMS_FORM)
    print(f"All passengers reply to {num_custom_declarations} questions with 'yes'.")

    num_custom_declarations = count_custom_declaration(CUSTOMS_FORM, all_agree=True)
    print(f"All passengers reply to {num_custom_declarations} questions with 'yes' "
          f"considering everyone in one group needs to agree to the same question.")
