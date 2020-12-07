#!/usr/bin/env python3


def parse_input(input):
    db = []
    for line in input.readlines():
        entry = line.split(':', maxsplit=1)
        raw_policy = entry[0]
        pw = entry[1]

        db.append({'raw_policy': raw_policy, 'pw': pw})

    return db


def parse_policy(raw_policy):
    policy = {'bounds': [None, None], 'char': None}

    fields = raw_policy.split(' ', maxsplit=1)

    raw_bounds = fields[0].split('-', maxsplit=1)
    policy['bounds'] = [int(raw_bounds[0]), int(raw_bounds[1])]
    policy['char'] = fields[1]

    return policy


def is_valid(policy, pw):
    return pw.count(policy['char']) in range(policy['bounds'][0],
                                             policy['bounds'][1] + 1)


def count_valid_pws(db):
    count = 0
    for entry in db:
        if is_valid(parse_policy(entry['raw_policy']), entry['pw']):
            count += 1

    return count


def main(input, part, should_print=False):
    pw_db = parse_input(input)
    input.close()
    answers = [None, None]

    if not part or part == 1:
        answers[0] = count_valid_pws(pw_db)
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
