import argparse
import re
from collections import defaultdict
import itertools as it
import math
from hashlib import md5
from advent_of_code import lib
from copy import deepcopy

di = lib.di4
dj = lib.dj4

parser = argparse.ArgumentParser()
parser.add_argument("input")
parser.add_argument("part", type=int)
args = parser.parse_args()

f = open(args.input, "r")
lines = [line for line in f.read().splitlines() if line.strip()]

fl = 0
for i, c in enumerate(lines[0]):
    fl += 1 if c == '(' else -1
    if args.part == 2 and fl == -1:
        print(i+1)
        exit(0)
print(fl)
