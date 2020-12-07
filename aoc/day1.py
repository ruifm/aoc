#!/usr/bin/env python3


def file2list(file):
    output = []
    for entry in file.readlines():
        output.append(int(entry))

    return output


def compute_answer(entries, nb_elements=2, sum_to=2020):
    cache = []
    for entry in entries:
        complement = sum_to - entry
        if nb_elements == 2:
            for cached_entry in cache:
                if cached_entry == complement:
                    return entry * complement
            cache.append(entry)
        else:
            sub_product = compute_answer(entries, nb_elements - 1, complement)
            if sub_product:
                return sub_product * entry

    return None


def main(input, part, should_print=False):
    report = file2list(input)
    input.close()
    answers = [None, None]

    if not part or part == 1:
        answers[0] = compute_answer(report, 2)
        if should_print:
            print(answers[0])
        if part:
            return answers[0]

    if not part or part == 2:
        answers[1] = compute_answer(report, 3)
        if should_print:
            print(answers[1])
        if part:
            return answers[1]

    return answers
