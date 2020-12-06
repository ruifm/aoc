#!/usr/bin/env python3

import sys
import argparse
from pathlib import Path



def get_default_input(day):
    return (Path(__file__).parent.parent /
            Path('inputs/day' + str(day) + '.txt')).open()


def get_args(day):
    parser = argparse.ArgumentParser(description='Compute day ' + str(day) +
                                     ' answers')
    parser.add_argument('-p', '--part', type=int,
                        choices=[1, 2],
                        help="Filter the answer the by the part number")
    parser.add_argument('inputfile', nargs='?', type=argparse.FileType('r'),
                        default=(get_default_input(day)
                                 if sys.stdin.isatty() else sys.stdin),
                        help=("if unspecified tries to read from stdin and if"
                              "that fails, it reads the default input file for"
                              "that day"))
    return parser.parse_args()
