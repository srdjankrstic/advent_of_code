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

f = open(args.input, "r")
lines = [line for line in f.read().splitlines() if line.strip()]

tlo = 17
thi = 61

unprocessed = set(range(len(lines)))
bots = defaultdict(set)
for li, line in enumerate(lines):
    nums = lib.rints(line)
    if len(nums) == 2:
        bots[nums[1]].add(nums[0])
        unprocessed.remove(li)

outputs = defaultdict(set)
while(len(unprocessed)):
    rest = list(unprocessed)
    for ri in rest:
        nums = lib.rints(lines[ri])
        if len(bots[nums[0]]) >= 2:
            unprocessed.remove(ri)
            lo = min(bots[nums[0]])
            hi = max(bots[nums[0]])
            bots[nums[0]].remove(lo)
            bots[nums[0]].remove(hi)
            if "low to bot" in lines[ri]:
                bots[nums[1]].add(lo)
            else:
                outputs[nums[1]].add(lo)
            if "high to bot" in lines[ri]:
                bots[nums[2]].add(hi)
            else:
                outputs[nums[1]].add(hi)
            if lo == tlo and hi == thi:
                print(nums[0])
if args.part == 2:
    print(outputs[0])
    print(outputs[1])
    print(outputs[2])
    print(outputs[0].pop() * outputs[1].pop() * outputs[2].pop())
