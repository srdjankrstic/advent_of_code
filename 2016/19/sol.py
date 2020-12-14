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

inp = lib.rints(lines[0])[0]

if args.part == 1:
    z = int("0"+lib.bin1(inp)[1:], 2)
    print(2 * z + 1)
elif args.part == 2:
    surv = [0]
    for i in range(2, inp + 1):
        kill = i // 2
        if surv[-1] + 1 < kill:
            surv.append((surv[-1] + 1) % i)
        else:
            surv.append((surv[-1] + 2) % i)
    print(surv[-1] + 1)
