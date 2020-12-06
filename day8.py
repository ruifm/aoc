#!/usr/bin/env python3

import utils


def main(input, part, should_print=False):
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


if __name__ == "__main__":
    args = utils.get_args(8)
    main(args.inputfile, args.part, True)
