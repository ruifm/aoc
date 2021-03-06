#!/usr/bin/env python3


def main(input, part, should_print=False):
    input.close()
    answers = [None, None]

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
