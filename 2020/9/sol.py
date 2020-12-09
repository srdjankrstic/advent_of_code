import argparse
import re
from collections import defaultdict
import itertools as it
import math


def solve1(lines):
    sol = 0
    nums = []
    pre = 5 if args.part == 1 else 25
    n = 0
    for line in lines.splitlines():
        if not line:
            break
        nums.append(int(line))
    n = len(nums)
    for i in range(pre, n):
        ok = False
        for j in range(pre):
            for k in range(pre):
                if j == k:
                    continue
                if nums[i - j - 1] + nums[i - k - 1] == nums[i]:
                    ok = True
                    break
        if not ok:
            return nums[i]


def solve2(lines):
    sol1 = solve1(lines)
    nums = []
    for line in lines.splitlines():
        if not line:
            break
        nums.append(int(line))
    n = len(nums)
    sums = [0] * n
    sums[0] = nums[0]
    for i in range(1, n):
        sums[i] = sums[i - 1] + nums[i]
        for j in range(i):
            if sums[i] - sums[j] == sol1:
                return min(nums[j+1:i+1]) + max(nums[j+1:i+1])


parser = argparse.ArgumentParser()
parser.add_argument("input")
parser.add_argument("part", type=int)
args = parser.parse_args()

f = open(args.input, "r")
lines = f.read()

if True:  # and args.part == 1:
    print(solve1(lines))
if True:  # and args.part == 2:
    print(solve2(lines))
