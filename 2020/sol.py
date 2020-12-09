import argparse
import re
from collections import defaultdict
import itertools as it
import math


def solve1(lines):
    sol = 0
    for line in lines.splitlines():
        pass
    return sol


def solve2(lines):
    sol = 0
    for line in lines.splitlines():
        pass
    return sol


parser = argparse.ArgumentParser()
parser.add_argument("input")
parser.add_argument("part", type=int)
args = parser.parse_args()

f = open(args.input, "r")
lines = f.read()

if True:  # and args.part == 1:
    print(solve1(lines))
if True:  # and args.part == 2:
    print(solve2(lines))
