#!/usr/bin/env python3

import re
from typing import List, Optional

RULE_PATTERN = re.compile(r"^([^\t\n\r\f\v]+) bags contain([^\t\n\r\f\v]+)\.$")
ELEMENT_PATTERN = re.compile(r"^ ([0-9]+) ([^\t\n\r\f\v]+) bags?$")


def build_tree(input):
    tree = {}
    tree_inverted = {}
    for line in input.readlines():
        matches = RULE_PATTERN.findall(line.strip())[0]
        subject = matches[0]
        predicate = matches[1]

        if subject not in tree.keys():
            tree[subject] = []
        if subject not in tree_inverted.keys():
            tree_inverted[subject] = []

        if predicate == " no other bags":
            continue

        for raw_child in predicate.split(","):
            child_matches = ELEMENT_PATTERN.findall(raw_child)[0]
            count = int(child_matches[0])
            color = child_matches[1]
            if color not in tree.keys():
                tree[color] = []
            if color not in tree_inverted.keys():
                tree_inverted[color] = []

            tree[subject].append({"count": count, "color": color})
            tree_inverted[color].append({"count": count, "color": subject})

    return tree, tree_inverted


def visit_node_types(tree, node="shiny gold", different_children=[]):
    for child in tree[node]:
        if child["color"] in different_children:
            continue
        different_children.append(child["color"])
        different_children = visit_node_types(
            tree, child["color"], different_children
        )
    return different_children


def visit_node_count(tree, node="shiny gold"):
    count = 0
    for child in tree[node]:
        count += child["count"] * (1 + visit_node_count(tree, child["color"]))
    return count


def main(input, part, should_print=False):
    normal_tree, inverted_tree = build_tree(input)
    input.close()
    answers: List[Optional[int]] = [None, None]

    if not part or part == 1:
        answers[0] = len(visit_node_types(inverted_tree))
        if should_print:
            print(answers[0])
        if part:
            return answers[0]

    if not part or part == 2:
        answers[1] = visit_node_count(normal_tree)
        if should_print:
            print(answers[1])
        if part:
            return answers[1]

    return answers
