import argparse
import re
from collections import defaultdict
import itertools as it
import math
from hashlib import md5
from advent_of_code import lib
from copy import deepcopy
import numpy as np
import json

di = lib.di4
dj = lib.dj4

parser = argparse.ArgumentParser()
parser.add_argument("input")
parser.add_argument("part", type=int)
args = parser.parse_args()

f = open(args.input, "r")
lines = [line for line in f.read().splitlines() if line.strip()]

endtime = 2503
#endtime = 1000

best = 0
pos = []
for li, line in enumerate(lines):
    [spd, fly, rest] = lib.rints(line)
    if args.part == 1:
        x = fly * spd
        t = x * (endtime // (fly + rest)) + spd * min(fly, (endtime % (fly + rest)))
        best = max(best, t)
    else:
        left = fly
        pace = spd
        pp = [0]
        for time in range(endtime):
            pp.append(pp[-1] + pace)
            left -= 1
            if left == 0 and pace == spd:
                left = rest
                pace = 0
            elif left == 0 and pace == 0:
                left = fly
                pace = spd
        pos.append(pp)

if args.part == 2:
    totalpts = [0] * len(pos)
    for time in range(1, endtime + 1):
        m = 0; mi = 0
        for j in range(len(pos)):
            if pos[j][time] > m:
                m = pos[j][time]
                mi = j
        totalpts[mi] += 1
    best = max(totalpts)

print(best)
