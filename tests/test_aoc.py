#!/usr/bin/env python3

import unittest
from pathlib import Path
from context import aoc


def get_default_test_input(day):
    return (Path(__file__).parent /
            Path('inputs/day' + str(day) + '.txt')).open()


class TestAoC(unittest.TestCase):

    def test_day1_part1(self):
        self.assertEqual(aoc.aoc.run_day(1, 1, get_default_test_input(1)),
                         514579)

    def test_day1_part2(self):
        self.assertEqual(aoc.aoc.run_day(1, 2, get_default_test_input(1)),
                         241861950)

    def test_day2_part1(self):
        self.assertEqual(aoc.aoc.run_day(2, 1, get_default_test_input(2)), 2)

    def test_day2_part2(self):
        self.assertIsNone(aoc.aoc.run_day(2, 2, get_default_test_input(2)))

    def test_day3_part1(self):
        self.assertIsNone(aoc.aoc.run_day(3, 1, get_default_test_input(3)))

    def test_day3_part2(self):
        self.assertIsNone(aoc.aoc.run_day(3, 2, get_default_test_input(3)))

    def test_day4_part1(self):
        self.assertIsNone(aoc.aoc.run_day(4, 1, get_default_test_input(4)))

    def test_day4_part2(self):
        self.assertIsNone(aoc.aoc.run_day(4, 2, get_default_test_input(4)))

    def test_day5_part1(self):
        self.assertIsNone(aoc.aoc.run_day(5, 1, get_default_test_input(5)))

    def test_day5_part2(self):
        self.assertIsNone(aoc.aoc.run_day(5, 2, get_default_test_input(5)))

    def test_day6_part1(self):
        self.assertIsNone(aoc.aoc.run_day(6, 1, get_default_test_input(6)))

    def test_day6_part2(self):
        self.assertIsNone(aoc.aoc.run_day(6, 2, get_default_test_input(6)))

    def test_day7_part1(self):
        self.assertIsNone(aoc.aoc.run_day(7, 1, get_default_test_input(7)))

    def test_day7_part2(self):
        self.assertIsNone(aoc.aoc.run_day(7, 2, get_default_test_input(7)))

    def test_day8_part1(self):
        self.assertIsNone(aoc.aoc.run_day(8, 1, get_default_test_input(8)))

    def test_day8_part2(self):
        self.assertIsNone(aoc.aoc.run_day(8, 2, get_default_test_input(8)))

    def test_day9_part1(self):
        self.assertIsNone(aoc.aoc.run_day(9, 1, get_default_test_input(9)))

    def test_day9_part2(self):
        self.assertIsNone(aoc.aoc.run_day(9, 2, get_default_test_input(9)))

    def test_day10_part1(self):
        self.assertIsNone(aoc.aoc.run_day(10, 1, get_default_test_input(10)))

    def test_day10_part2(self):
        self.assertIsNone(aoc.aoc.run_day(10, 2, get_default_test_input(10)))

    def test_day11_part1(self):
        self.assertIsNone(aoc.aoc.run_day(11, 1, get_default_test_input(11)))

    def test_day11_part2(self):
        self.assertIsNone(aoc.aoc.run_day(11, 2, get_default_test_input(11)))

    def test_day12_part1(self):
        self.assertIsNone(aoc.aoc.run_day(12, 1, get_default_test_input(12)))

    def test_day12_part2(self):
        self.assertIsNone(aoc.aoc.run_day(12, 2, get_default_test_input(12)))

    def test_day13_part1(self):
        self.assertIsNone(aoc.aoc.run_day(13, 1, get_default_test_input(13)))

    def test_day13_part2(self):
        self.assertIsNone(aoc.aoc.run_day(13, 2, get_default_test_input(13)))

    def test_day14_part1(self):
        self.assertIsNone(aoc.aoc.run_day(14, 1, get_default_test_input(14)))

    def test_day14_part2(self):
        self.assertIsNone(aoc.aoc.run_day(14, 2, get_default_test_input(14)))

    def test_day15_part1(self):
        self.assertIsNone(aoc.aoc.run_day(15, 1, get_default_test_input(15)))

    def test_day15_part2(self):
        self.assertIsNone(aoc.aoc.run_day(15, 2, get_default_test_input(15)))

    def test_day16_part1(self):
        self.assertIsNone(aoc.aoc.run_day(16, 1, get_default_test_input(16)))

    def test_day16_part2(self):
        self.assertIsNone(aoc.aoc.run_day(16, 2, get_default_test_input(16)))

    def test_day17_part1(self):
        self.assertIsNone(aoc.aoc.run_day(17, 1, get_default_test_input(17)))

    def test_day17_part2(self):
        self.assertIsNone(aoc.aoc.run_day(17, 2, get_default_test_input(17)))

    def test_day18_part1(self):
        self.assertIsNone(aoc.aoc.run_day(18, 1, get_default_test_input(18)))

    def test_day18_part2(self):
        self.assertIsNone(aoc.aoc.run_day(18, 2, get_default_test_input(18)))

    def test_day19_part1(self):
        self.assertIsNone(aoc.aoc.run_day(19, 1, get_default_test_input(19)))

    def test_day19_part2(self):
        self.assertIsNone(aoc.aoc.run_day(19, 2, get_default_test_input(19)))

    def test_day20_part1(self):
        self.assertIsNone(aoc.aoc.run_day(20, 1, get_default_test_input(20)))

    def test_day20_part2(self):
        self.assertIsNone(aoc.aoc.run_day(20, 2, get_default_test_input(20)))

    def test_day21_part1(self):
        self.assertIsNone(aoc.aoc.run_day(21, 1, get_default_test_input(21)))

    def test_day21_part2(self):
        self.assertIsNone(aoc.aoc.run_day(21, 2, get_default_test_input(21)))

    def test_day22_part1(self):
        self.assertIsNone(aoc.aoc.run_day(22, 1, get_default_test_input(22)))

    def test_day22_part2(self):
        self.assertIsNone(aoc.aoc.run_day(22, 2, get_default_test_input(22)))

    def test_day23_part1(self):
        self.assertIsNone(aoc.aoc.run_day(23, 1, get_default_test_input(23)))

    def test_day23_part2(self):
        self.assertIsNone(aoc.aoc.run_day(23, 2, get_default_test_input(23)))

    def test_day24_part1(self):
        self.assertIsNone(aoc.aoc.run_day(24, 1, get_default_test_input(24)))

    def test_day24_part2(self):
        self.assertIsNone(aoc.aoc.run_day(24, 2, get_default_test_input(24)))


if __name__ == '__main__':
    unittest.main()
