from aoc2020.day_2.password_database import password_database


def validate_password_database(password_database, toboggan_style=True):
    passwords_with_policy = _preprocess_password_database(password_database)
    valid_passwords = []
    for password in passwords_with_policy:
        policy = _validate_password_toboggan_style if toboggan_style else _validate_password_old_style
        if policy(password):
            valid_passwords.append(password)
    return valid_passwords


def _preprocess_password_database(password_database):
    lines = password_database.splitlines()
    passwords_with_policy = []
    for line in lines:
        passwords_with_policy.append(_get_password_with_policy(line))
    return passwords_with_policy


def _get_password_with_policy(line):
    limits, letter, password = line.split(" ")
    lower_limit, upper_limit = limits.split("-")
    letter = letter.strip(":")
    return {
        "lower_limit": lower_limit,
        "upper_limit": upper_limit,
        "letter": letter,
        "password": password,
    }


def _validate_password_old_style(password) -> bool:
    occurrence = password["password"].count(password["letter"])
    res = occurrence >= int(password["lower_limit"]) and occurrence <= int(password["upper_limit"])
    return res


def _validate_password_toboggan_style(password) -> bool:
    index_a = int(password["lower_limit"]) - 1  # no zero-indexing
    index_b = int(password["upper_limit"]) - 1  # no zero-indexing
    letter = password["letter"]
    password = password["password"]
    if password[index_a] == letter and password[index_b] != letter:
        return True
    if password[index_a] != letter and password[index_b] == letter:
        return True
    return False


if __name__ == '__main__':
    print("Day 2")
    valid_passwords = validate_password_database(password_database, False)
    print(f"There are {len(valid_passwords)} valid passwords in the database respecting old style validation.")
    valid_passwords = validate_password_database(password_database, True)
    print(f"There are {len(valid_passwords)} valid passwords in the database respecting Toboggan style validation.")
