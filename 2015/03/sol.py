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

mp = "^>v<"
seen = set()
pos = (0, 0)
posr = (0, 0)
for i, c in enumerate(lines[0]):
    if args.part == 1:
        if pos not in seen:
            seen.add(pos)
        d = mp.index(c)
        pos = (pos[0] + di[d], pos[1] + dj[d])
    else:
        if i % 2:
            if pos not in seen:
                seen.add(pos)
            d = mp.index(c)
            pos = (pos[0] + di[d], pos[1] + dj[d])
        else:
            if posr not in seen:
                seen.add(posr)
            d = mp.index(c)
            posr = (posr[0] + di[d], posr[1] + dj[d])
print(len(seen))
