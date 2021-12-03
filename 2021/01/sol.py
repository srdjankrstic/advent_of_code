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

nums = []
for li, line in enumerate(lines):
    nums.extend(lib.rints(line))

sol = 0

if args.part == 1:
    for i in range(1, len(nums)):
        if nums[i] > nums[i-1]:
            sol += 1
else:
    sum1 = nums[0] + nums[1] + nums[2]
    for i in range(3, len(nums)):
        newsum = sum1 - nums[i-3] + nums[i]
        if newsum > sum1:
            sol += 1
        sum1 = newsum

print(sol)
