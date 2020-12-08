#!/usr/bin/env python3


def is_tree(raw_map, x, y):
    row = raw_map[y].strip()
    return row[x % len(row)] == '#'


def count_trees(raw_map, step):
    nb_trees = 0
    x = 0
    y = 0
    while y < len(raw_map):
        if is_tree(raw_map, x, y):
            nb_trees += 1
        x += step[0]
        y += step[1]

    return nb_trees


def main(input, part, should_print=False):
    raw_map = input.readlines()
    input.close()
    answers = [None, None]

    if not part or part == 1:
        answers[0] = count_trees(raw_map, [3, 1])
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
