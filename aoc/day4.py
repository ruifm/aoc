#!/usr/bin/env python3

import re

FIELDS = [
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid",
    "cid",
]


def create_passport():
    return {field: None for field in FIELDS}


def is_field_valid(field, value, strict):
    if field == "cid":
        return True

    if not value:
        return False

    if not strict:
        return True

    year_pattern = re.compile("[0-9]{4}")
    if field == "byr":
        return year_pattern.fullmatch(value) and (1920 <= int(value) <= 2002)

    if field == "iyr":
        return year_pattern.fullmatch(value) and (2010 <= int(value) <= 2020)

    if field == "eyr":
        return year_pattern.fullmatch(value) and (2020 <= int(value) <= 2030)

    if field == "hgt":
        if re.compile("[0-9]+cm").fullmatch(value):
            height = int(value.rstrip("cm"))
            return 150 <= height <= 193
        elif re.compile("[0-9]+in").fullmatch(value):
            height = int(value.rstrip("in"))
            return 59 <= height <= 76
        else:
            return False

    if field == "hcl":
        return re.compile("#[0-9a-f]{6}").fullmatch(value)

    if field == "ecl":
        return value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

    if field == "pid":
        return re.compile("[0-9]{9}").fullmatch(value)

    return False


def parse_input(input):
    passports = []
    passport = create_passport()
    for row in input.readlines():
        if row == "\n":
            passports.append(passport)
            passport = create_passport()
            continue

        for field in row.split():
            pair = field.split(":", 1)
            passport[pair[0]] = pair[1]

    passports.append(passport)
    return passports


def is_valid(passport, strict):
    for field in FIELDS:
        if not is_field_valid(field, passport[field], strict):
            return False

    return True


def count_valid_passports(passports, strict):
    nb_valid = 0
    for passport in passports:
        if is_valid(passport, strict):
            nb_valid += 1

    return nb_valid


def main(input, part, should_print=False):
    passports = parse_input(input)
    input.close()
    answers = [None, None]

    if not part or part == 1:
        answers[0] = count_valid_passports(passports, strict=False)
        if should_print:
            print(answers[0])
        if part:
            return answers[0]

    if not part or part == 2:
        answers[1] = count_valid_passports(passports, strict=True)
        if should_print:
            print(answers[1])
        if part:
            return answers[1]

    return answers
