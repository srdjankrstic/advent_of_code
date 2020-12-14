import argparse
import re
from collections import defaultdict
import itertools as it
import math
from hashlib import md5
from advent_of_code import lib
from copy import deepcopy
import pdb

parser = argparse.ArgumentParser()
parser.add_argument("input")
parser.add_argument("part", type=int)
args = parser.parse_args()

f = open(args.input, "r")
lines = [line for line in f.read().splitlines() if line.strip()]

inp = lines[0]

last = defaultdict(list)
keys = []
for i in it.count(0):
    if args.part == 1:
        h = lib.hmd5(inp, i)
    elif args.part == 2:
        h = inp + str(i)
        for _ in range(2017):
            h = lib.hmd5(h)
    for j in range(4, len(h)):
        if h[j] == h[j-1] and h[j] == h[j-2] and h[j] == h[j-3] and h[j] == h[j-4]:
            cp = deepcopy(last[h[j]])
            for pos in last[h[j]]:
                if i - pos > 1000:
                    cp.remove(pos)
                elif pos not in keys:
                    keys.append(pos)
                    cp.remove(pos)
#                    print(len(keys))
                    if len(keys) > 72:
#                        print(sorted(keys))
                        print(sorted(keys)[63])
                        exit(0)
            last[h[j]] = cp
    for j in range(2, len(h)):
        if h[j] == h[j-1] and h[j] == h[j-2]:
            last[h[j]].append(i)
            break
