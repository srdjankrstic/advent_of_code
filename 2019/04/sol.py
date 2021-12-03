import argparse
import re
from collections import defaultdict
from functools import reduce
import itertools as it
import math
from hashlib import md5
from advent_of_code import lib
from copy import deepcopy
import numpy as np
import json
import sympy.ntheory.factor_

di = lib.di4
dj = lib.dj4

parser = argparse.ArgumentParser()
parser.add_argument("input")
parser.add_argument("part", type=int)
args = parser.parse_args()

f = open(args.input, "r")
lines = [line for line in f.read().splitlines() if line.strip()]

def good(x):
    digs = []
    runs = []
    run = 1
    while x:
        digs.append(x%10)
        x //= 10
    digs.reverse()
    for i in range(1, len(digs)):
        if digs[i] == digs[i-1]:
            run += 1
        else:
            if run > 1:
                runs.append(run)
            run = 1
        if digs[i] < digs[i-1]:
            return False
    if run > 1:
        runs.append(run)
    if args.part == 1:
        return len(runs) > 0
    else:
        return 2 in runs


for li, line in enumerate(lines):
    nums = lib.rints(line)
    print(sum([1 if good(x) else 0 for x in  range(nums[0], nums[1])]))
