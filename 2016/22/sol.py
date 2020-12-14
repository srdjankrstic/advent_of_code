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

used = []; avail = []; usedd = {}; totald = {}

for li, line in enumerate(lines):
    if li > 1:
        r = lib.rints(line)
        used.append(r[3])
        avail.append(r[4])
        usedd[(r[0], r[1])] = r[3]
        totald[(r[0], r[1])] = r[3] + r[4]

if args.part == 1:
    via = 0
    for i in range(len(used)):
        for j in range(len(used)):
            if i != j and used[i] and used[i] <= avail[j]:
                via += 1
    print(via)
else:
    for i in range(38):
        for j in range(28):
            print(f"{usedd[(i, j)]}/{totald[(i, j)]}\t", end="")
        print("")
