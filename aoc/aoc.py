#!/usr/bin/env python3

from pathlib import Path
import argparse
import sys

from . import day1
from . import day2
from . import day3
from . import day4
from . import day5
from . import day6
from . import day7
from . import day8
from . import day9
from . import day10
from . import day11
from . import day12
from . import day13
from . import day14
from . import day15
from . import day16
from . import day17
from . import day18
from . import day19
from . import day20
from . import day21
from . import day22
from . import day23
from . import day24


def get_args():
    parser = argparse.ArgumentParser(description='Compute AoC 2020 answers')
    parser.add_argument('-p', '--part', type=int,
                        choices=[1, 2],
                        help="Filter the answer the by the part number")
    parser.add_argument('-d', '--day', type=int,
                        choices=range(1, 25),
                        help="Filter the answer the by the advent day")
    parser.add_argument('inputfile', nargs='?', type=argparse.FileType('r'),
                        default=(None
                                 if sys.stdin.isatty() else sys.stdin),
                        help=("if unspecified tries to read from stdin and if"
                              "that fails, it reads the default input file for"
                              "that day"))
    return parser.parse_args()


def get_default_input(day):
    return (Path(__file__).parent.parent /
            Path('inputs/day' + str(day) + '.txt')).open()


def run_day(day, part=None, input=None):
    inputfile = input if input else get_default_input(day)
    if day == 1:
        return day1.main(inputfile, part)
    elif day == 2:
        return day2.main(inputfile, part)
    elif day == 3:
        return day3.main(inputfile, part)
    elif day == 4:
        return day4.main(inputfile, part)
    elif day == 5:
        return day5.main(inputfile, part)
    elif day == 6:
        return day6.main(inputfile, part)
    elif day == 7:
        return day7.main(inputfile, part)
    elif day == 8:
        return day8.main(inputfile, part)
    elif day == 9:
        return day9.main(inputfile, part)
    elif day == 10:
        return day10.main(inputfile, part)
    elif day == 11:
        return day11.main(inputfile, part)
    elif day == 12:
        return day12.main(inputfile, part)
    elif day == 13:
        return day13.main(inputfile, part)
    elif day == 14:
        return day14.main(inputfile, part)
    elif day == 15:
        return day15.main(inputfile, part)
    elif day == 16:
        return day16.main(inputfile, part)
    elif day == 17:
        return day17.main(inputfile, part)
    elif day == 18:
        return day18.main(inputfile, part)
    elif day == 19:
        return day19.main(inputfile, part)
    elif day == 20:
        return day20.main(inputfile, part)
    elif day == 21:
        return day21.main(inputfile, part)
    elif day == 22:
        return day22.main(inputfile, part)
    elif day == 23:
        return day23.main(inputfile, part)
    elif day == 24:
        return day24.main(inputfile, part)


def main():
    args = get_args()

    if not args.day:
        for d in range(1, 25):
            print(d, '\t:', run_day(d, args.part, args.inputfile))
    else:
        print(run_day(args.day, args.part, args.inputfile))
