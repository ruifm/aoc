#!/usr/bin/env python3

def create_negative_answer():
    return [False for i in range(26)]

def parse_input(input):
    groups = []
    group = []
    for line in input.readlines():
        if line == '\n' and len(group) > 0:
            groups.append(group)
            group = []
            continue

        answer = create_negative_answer()
        for char in line.strip():
            answer[ord(char) - ord('a')] = True
        group.append(answer)

    groups.append(group)
    return groups


def or_in_group(group):
    combined = create_negative_answer()
    for answer in group:
        for i in range(26):
            combined[i] |= answer[i]

    return combined


def count_yes(groups):
    collapsed = [or_in_group(group).count(True) for group in groups]
    return sum(collapsed)


def main(input, part, should_print=False):
    groups = parse_input(input)
    input.close()
    answers = [None, None]

    if not part or part == 1:
        answers[0] = count_yes(groups)
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
