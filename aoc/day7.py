#!/usr/bin/env python3

import re

RULE_PATTERN = re.compile(r"^([^\t\n\r\f\v]+) bags contain([^\t\n\r\f\v]+)\.$")


def parse_rules(input):
    rules = {}
    for line in input.readlines():
        matches = RULE_PATTERN.findall(line.strip())
        rules[matches[0][0]] = matches[0][1]

    return rules


def main(input, part, should_print=False):
    rules = parse_rules(input)
    input.close()
    answers = [None, None]

    print(rules)
    if not part or part == 1:
        answers[0] = None
        if should_print:
            print(answers[0])
        if part:
            return answers[0]

    if not part or part == 2:
        answers[1] = None
        if should_print:
            print(answers[1])
        if part:
            return answers[1]

    return answers
