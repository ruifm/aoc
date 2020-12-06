#!/usr/bin/env python3

import argparse

import day1
import day2
import day3
import day4
import day5
import day6
import day7
import day8
import day9
import day10
import day11
import day12
import day13
import day14
import day15
import day16
import day17
import day18
import day19
import day20
import day21
import day22
import day23
import day24


def get_args():
    parser = argparse.ArgumentParser(description='Compute AoC 2020 answers')
    parser.add_argument('-p', '--part', type=int,
                        choices=[1, 2],
                        help="Filter the answer the by the part number")
    parser.add_argument('-d', '--day', type=int,
                        choices=range(25),
                        help="Filter the answer the by the advent day")
    return parser.parse_args()


def main():
    args = get_args()

    if not args.day or args.day == 1:
        with open("inputs/day1.txt") as inputfile:
            day1.main(inputfile, args.part, True)
    if not args.day or args.day == 2:
        with open("inputs/day2.txt") as inputfile:
            day2.main(inputfile, args.part, True)
    if not args.day or args.day == 3:
        with open("inputs/day3.txt") as inputfile:
            day3.main(inputfile, args.part, True)
    if not args.day or args.day == 4:
        with open("inputs/day4.txt") as inputfile:
            day4.main(inputfile, args.part, True)
    if not args.day or args.day == 5:
        with open("inputs/day5.txt") as inputfile:
            day5.main(inputfile, args.part, True)
    if not args.day or args.day == 6:
        with open("inputs/day6.txt") as inputfile:
            day6.main(inputfile, args.part, True)
    if not args.day or args.day == 7:
        with open("inputs/day7.txt") as inputfile:
            day7.main(inputfile, args.part, True)
    if not args.day or args.day == 8:
        with open("inputs/day8.txt") as inputfile:
            day8.main(inputfile, args.part, True)
    if not args.day or args.day == 9:
        with open("inputs/day9.txt") as inputfile:
            day9.main(inputfile, args.part, True)
    if not args.day or args.day == 10:
        with open("inputs/day10.txt") as inputfile:
            day10.main(inputfile, args.part, True)
    if not args.day or args.day == 11:
        with open("inputs/day11.txt") as inputfile:
            day11.main(inputfile, args.part, True)
    if not args.day or args.day == 12:
        with open("inputs/day12.txt") as inputfile:
            day12.main(inputfile, args.part, True)
    if not args.day or args.day == 13:
        with open("inputs/day13.txt") as inputfile:
            day13.main(inputfile, args.part, True)
    if not args.day or args.day == 14:
        with open("inputs/day14.txt") as inputfile:
            day14.main(inputfile, args.part, True)
    if not args.day or args.day == 15:
        with open("inputs/day15.txt") as inputfile:
            day15.main(inputfile, args.part, True)
    if not args.day or args.day == 16:
        with open("inputs/day16.txt") as inputfile:
            day16.main(inputfile, args.part, True)
    if not args.day or args.day == 17:
        with open("inputs/day17.txt") as inputfile:
            day17.main(inputfile, args.part, True)
    if not args.day or args.day == 18:
        with open("inputs/day18.txt") as inputfile:
            day18.main(inputfile, args.part, True)
    if not args.day or args.day == 19:
        with open("inputs/day19.txt") as inputfile:
            day19.main(inputfile, args.part, True)
    if not args.day or args.day == 20:
        with open("inputs/day20.txt") as inputfile:
            day20.main(inputfile, args.part, True)
    if not args.day or args.day == 21:
        with open("inputs/day21.txt") as inputfile:
            day21.main(inputfile, args.part, True)
    if not args.day or args.day == 22:
        with open("inputs/day22.txt") as inputfile:
            day22.main(inputfile, args.part, True)
    if not args.day or args.day == 23:
        with open("inputs/day23.txt") as inputfile:
            day23.main(inputfile, args.part, True)
    if not args.day or args.day == 24:
        with open("inputs/day24.txt") as inputfile:
            day24.main(inputfile, args.part, True)


if __name__ == "__main__":
    main()
