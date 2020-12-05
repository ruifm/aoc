#!/usr/bin/env python3

import numpy as np
import sys


def file2list(filename):
    output = []
    with open(filename) as file:
        for entry in file.readlines():
            output.append(int(entry))

    return output


def compute_product_pair(entries, sum_to=2020):
    complements = sum_to - np.array(entries)
    products = complements * entries
    cache = []
    for product in products:
        for cached_product in cache:
            if cached_product == product:
                return product

        cache.append(product)

    return -1


def compute_product_trio(entries, sum_to=2020):
    complements = sum_to - np.array(entries)
    for i in range(len(entries)):
        entry = entries[i]
        complement = complements[i]
        sub_product = compute_product_pair(entries, complement)
        if sub_product != -1:
            return sub_product * entry

    return -1


def main():
    filename = "full_report.txt"
    if len(sys.argv) > 1:
        filename = sys.argv[1]

    report = file2list(filename)

    print("Part 1: ", compute_product_pair(report))
    print("Part 2: ", compute_product_trio(report))


if __name__ == "__main__":
    main()
