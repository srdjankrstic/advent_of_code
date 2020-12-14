import argparse
import re
from collections import defaultdict
import itertools as it
import math
from advent_of_code import lib


parser = argparse.ArgumentParser()
parser.add_argument("input")
parser.add_argument("part", type=int)
args = parser.parse_args()

f = open(args.input, "r")
lines = f.read()

if args.part == 1:
    c = 0
    for line in lines.splitlines():
        if not line.strip():
            continue
        nums = lib.rints(line)
        v = True
        for p in it.permutations(nums):
            if p[0] + p[1] <= p[2]:
                v = False
        if v:
            c += 1
    print(c)
else:
    c = 0
    nums = []
    for line in lines.splitlines():
        if not line.strip():
            continue
        nums.append(lib.rints(line))
    for i in range(len(nums[0])):
        j = 0
        while j < len(nums):
            tt = [nums[j][i], nums[j+1][i], nums[j+2][i]]
            v = True
            for p in it.permutations(tt):
                if p[0] + p[1] <= p[2]:
                    v = False
            if v:
                c += 1
            j += 3
    print(c)
