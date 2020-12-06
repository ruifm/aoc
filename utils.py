#!/usr/bin/env python3

import sys
import argparse


def get_args(day):
    parser = argparse.ArgumentParser(description='Compute day ' + str(day) +
                                     ' answers')
    parser.add_argument('-p', '--part', type=int,
                        choices=[1, 2],
                        help="Filter the answer the by the part number")
    parser.add_argument('inputfile', nargs='?', type=argparse.FileType('r'),
                        default=sys.stdin,
                        help="if not specified, reads from stdin")
    return parser.parse_args()
