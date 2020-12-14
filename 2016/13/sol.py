import argparse
import re
from collections import defaultdict
import itertools as it
import math
from hashlib import md5
from advent_of_code import lib
from copy import deepcopy


parser = argparse.ArgumentParser()
parser.add_argument("input")
parser.add_argument("part", type=int)
args = parser.parse_args()

def wall(x, y, f):
    z = x*x + 3*x + 2*x*y + y + y*y + f
    return lib.popcnt(z) % 2 == 1

f = open(args.input, "r")
lines = [line for line in f.read().splitlines() if line.strip()]

fav = int(lines[0])
target = (31, 39)

di = lib.di4; dj = lib.dj4
q = [((1, 1), 0)]
seen = set([(1, 1)])

while len(q) > 0:
    cur = q.pop(0)
    if args.part == 1:
        if cur[0] == target:
            print(cur[1])
            break
    elif args.part == 2:
        if cur[1] == 50:
            continue
    x = cur[0][0]; y = cur[0][1]
    for d in range(4):
        pi = x + di[d]; pj = y + dj[d]
        if pi < 0 or pj < 0:
            continue
        if (pi, pj) not in seen and not wall(pi, pj, fav):
            seen.add((pi, pj))
            q.append(((pi, pj), cur[1] + 1))
if args.part == 2:
    print(len(seen))