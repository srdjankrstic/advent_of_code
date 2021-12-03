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
TOT = 100

ing = dict()
for li, line in enumerate(lines):
    vs = lib.rnints(line)
    ing[li] = vs

best = 0

n = len(ing)

def take(sofar):
    global best
    s = sum(sofar)
    if len(sofar) == n - 1:
        sofar.append(100 - s)
        if sum([ing[x][4] * sofar[x] for x in range(n)]) == 500:
            this = 1
            for i in range(4):
                this *= max(0, sum([ing[x][i] * sofar[x] for x in range(n)]))
            best = max(best, this)
        sofar.pop()
    else:
        for x in range(101 - s):
            sofar.append(x)
            take(sofar)
            sofar.pop()

take([])
print(best)
