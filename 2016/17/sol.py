import argparse
import re
from collections import defaultdict
import itertools as it
import math
from hashlib import md5
from advent_of_code import lib
from copy import deepcopy

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

parser = argparse.ArgumentParser()
parser.add_argument("input")
parser.add_argument("part", type=int)
args = parser.parse_args()

f = open(args.input, "r")
lines = [line for line in f.read().splitlines() if line.strip()]

pwd = lines[0]

pmap = "UDLR"
q = [((0, 0), "")]

longest = 0
while len(q):
    cur = q.pop(0)
    if cur[0] == (3, 3):
        if args.part == 1:
            print(cur[1])
            break
        elif args.part == 2:
            longest = len(cur[1])
            continue
    s = lib.hmd5(pwd, cur[1])[:4]
    doors = [c in "bcdef" for c in s]
    x = cur[0][0]; y = cur[0][1]
    for d in range(4):
        pi = x + di[d]
        pj = y + dj[d]
        if not doors[d] or not 0 <= pi < 4 or not 0 <= pj < 4:
            continue
        q.append(((pi, pj), cur[1] + pmap[d]))

if args.part == 2:
    print(longest)