#!/usr/bin/env python3


def get_code(input):
    code = []
    for line in input.readlines():
        inst = line.strip().split()
        code.append({'op': inst[0], 'arg': int(inst[1])})

    return code


def handle_inst(inst):
    op = inst['op']
    arg = inst['arg']
    if op == 'acc':
        return 1, arg
    elif op == 'jmp':
        return arg, 0
    else:
        return 1, 0


def execute_until_loop(code):
    accumulator = 0
    addr = 0
    visited_addrs = []

    while addr not in visited_addrs:
        visited_addrs.append(addr)
        inst = code[addr]

        addr_offset, acc_offset = handle_inst(inst)

        addr += addr_offset
        accumulator += acc_offset

    return accumulator, visited_addrs


def flip_jmp_nop(inst):
    op = inst['op']
    arg = inst['arg']
    if op == 'nop':
        return {'op': 'jmp', 'arg': arg}
    elif op == 'jmp':
        return {'op': 'nop', 'arg': arg}


def execute_all(code):
    accumulator = 0
    addr = 0
    visited_addrs = []

    while addr < len(code):
        inst = code[addr]
        if addr in visited_addrs:
            return None
        visited_addrs.append(addr)

        addr_offset, acc_offset = handle_inst(inst)

        addr += addr_offset
        accumulator += acc_offset

    return accumulator


def remove_loop_and_execute(code):
    _, visited_addrs = execute_until_loop(code)

    for addr in visited_addrs:
        inst = code[addr]
        op = inst['op']
        arg = inst['arg']

        if op == 'acc':
            continue

        new_code = code.copy()
        new_code[addr] = flip_jmp_nop(inst)
        accumulator = execute_all(new_code)
        if accumulator is not None:
            return accumulator

    return None


def main(input, part, should_print=False):
    code = get_code(input)
    input.close()
    answers = [None, None]

    if not part or part == 1:
        answers[0], _ = execute_until_loop(code)
        if should_print:
            print(answers[0])
        if part:
            return answers[0]

    if not part or part == 2:
        answers[1] = remove_loop_and_execute(code)
        if should_print:
            print(answers[1])
        if part:
            return answers[1]

    return answers
