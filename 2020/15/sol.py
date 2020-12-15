import argparse
import re
from collections import defaultdict
import itertools as it
import math
from hashlib import md5
from advent_of_code import lib
from copy import deepcopy
import numpy as np

di = lib.di4
dj = lib.dj4

parser = argparse.ArgumentParser()
parser.add_argument("input")
parser.add_argument("part", type=int)
args = parser.parse_args()

f = open(args.input, "r")
lines = [line for line in f.read().splitlines() if line.strip()]

XX = 30000000 if args.part == 2 else 2020
for li, line in enumerate(lines):
    last = defaultdict(list)
    nums = lib.rints(line)
    spoken = [-1] * XX
    for i in range(XX):
        if i < len(nums):
            spoken[i] = nums[i]
            last[spoken[i]].append(i)
        elif len(last[spoken[i-1]]) == 1:
            spoken[i] = 0
            last[0].append(i)
        else:
            spoken[i] = last[spoken[i-1]][-1] - last[spoken[i-1]][-2]
            last[spoken[i]].append(i)

    print(spoken[-1])
