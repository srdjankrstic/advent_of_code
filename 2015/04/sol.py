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

target = "00000" if args.part == 1 else "000000"
for li, line in enumerate(lines):
    for i in it.count(0):
        if lib.hmd5(line, i).startswith(target):
            print(i)
            break
