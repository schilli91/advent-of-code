import re

from aoc2020.day_4.passports import PASSPORTS

PASSPORT_FIELDS = {
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid",
    # "cid",
}
VALID_EYE_COLOR = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth", }


def validate_passports(batch_file, strict=False):
    passport_candidates = _preprocess_batch_file(batch_file)

    if strict:
        return _validate_passports_strict(passport_candidates)

    return _validate_passports(passport_candidates)


def _preprocess_batch_file(batch_file: str):
    lines = batch_file.splitlines()

    passport_candidates = []
    candidate = ""
    for line in lines:
        if line == "":
            passport_candidates.append(candidate)
            candidate = ""
            continue
        candidate = f"{candidate} {line}".strip()
    passport_candidates.append(candidate)

    return passport_candidates


def _validate_candidate_fields(candidate):
    passport_keys = {pair.split(":")[0] for pair in candidate.split(" ")}

    intersection_with_required_fields = passport_keys.intersection(PASSPORT_FIELDS)
    return len(intersection_with_required_fields) == len(PASSPORT_FIELDS)


def _validate_passports(passport_candidates):
    number_valid_passports = 0
    for candidate in passport_candidates:
        if _validate_candidate_fields(candidate):
            number_valid_passports = number_valid_passports + 1

    return number_valid_passports


def _validate_passports_strict(passport_candidates):
    number_valid_passports = 0
    for candidate in passport_candidates:
        if not _validate_candidate_fields(candidate):
            continue
        if _validate_candidate_field_rules(candidate):
            number_valid_passports = number_valid_passports + 1

    return number_valid_passports


def _validate_candidate_field_rules(candidate):
    candidate_dict = {pair.split(":")[0]: pair.split(":")[1] for pair in candidate.split(" ")}

    if not _validate_byr(candidate_dict):
        return False
    if not _validate_iyr(candidate_dict):
        return False
    if not _validate_eyr(candidate_dict):
        return False
    if not _validate_hgt(candidate_dict):
        return False
    if not _validate_hcl(candidate_dict):
        return False
    if not _validate_ecl(candidate_dict):
        return False
    if not _validate_pid(candidate_dict):
        return False
    if not _validate_cid(candidate_dict):
        return False

    return True


def _validate_byr(candidate: dict):
    byr = candidate.get("byr", "")
    return _validate_number(byr, 4, 1920, 2002)


def _validate_iyr(candidate: dict):
    iyr = candidate.get("iyr", "")
    return _validate_number(iyr, 4, 2010, 2020)


def _validate_eyr(candidate: dict):
    eyr = candidate.get("eyr", "")
    return _validate_number(eyr, 4, 2020, 2030)


def _validate_hgt(candidate: dict):
    hgt = str(candidate.get("hgt", ""))
    if hgt == "":
        return False

    unit = hgt[-2:]
    if unit not in {"cm", "in"}:
        return False

    height = int(hgt[:-2])

    if unit == "cm":
        return 150 <= height <= 193
    if unit == "in":
        return 59 <= height <= 76
    return False


def _validate_hcl(candidate: dict):
    hcl = candidate.get("hcl", "")
    if len(hcl) > 7:
        return False
    pattern = r"\#([a-f]|[0-9]){6}"
    valid = re.match(pattern, hcl)
    if valid:
        return True
    return False


def _validate_ecl(candidate: dict):
    ecl = candidate.get("ecl", "")
    return ecl in VALID_EYE_COLOR


def _validate_pid(candidate: dict):
    pid = candidate.get("pid", "")
    if len(pid) > 9:
        return False

    pattern = r"[0-9]{9}"
    valid = re.match(pattern, pid)
    if valid:
        return True
    return False


def _validate_cid(candidate: dict):
    return True  # always passes


def _validate_number(number, digits, min, max):
    if len(number) != digits:
        return False
    number = int(number)
    return min <= number <= max


if __name__ == '__main__':
    print("Day 4")
    num_valid_passports = validate_passports(PASSPORTS)
    print(f"The passport data contains {num_valid_passports} valid passports that may lack the 'cid'.")
    num_valid_passports = validate_passports(PASSPORTS, strict=True)
    print(f"The passport data contains {num_valid_passports} valid passports complying all rules.")
