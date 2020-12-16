#!/usr/bin/env python3


def decode(input):
    input = input.replace("F", "0")
    input = input.replace("B", "1")
    input = input.replace("L", "0")
    input = input.replace("R", "1")
    return input


def parse_seats(input):
    seats = []
    for line in input.readlines():
        raw_seat = decode(line.strip())
        seats.append([int(raw_seat[:7], base=2), int(raw_seat[7:], base=2)])

    return seats


def to_seatid(seat):
    return 8 * seat[0] + seat[1]


def get_seatids(seats):
    return [to_seatid(seat) for seat in seats]


def max_seatid(seats):
    return max(get_seatids(seats))


def find_missing_id(ids):
    for id in range(1, max(ids)):
        if (id not in ids) and ((id - 1 in ids) and (id + 1 in ids)):
            return id

    return None


def main(input, part, should_print=False):
    seats = parse_seats(input)
    input.close()
    answers = [None, None]

    if not part or part == 1:
        answers[0] = max_seatid(seats)
        if should_print:
            print(answers[0])
        if part:
            return answers[0]

    if not part or part == 2:
        answers[1] = find_missing_id(get_seatids(seats))
        if should_print:
            print(answers[1])
        if part:
            return answers[1]

    return answers
