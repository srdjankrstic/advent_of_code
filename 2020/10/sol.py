import argparse
import re
from collections import defaultdict
import itertools as it
import math


parser = argparse.ArgumentParser()
parser.add_argument("input")
parser.add_argument("part", type=int)
args = parser.parse_args()

f = open(args.input, "r")
lines = f.read()

nums = [int(x) for x in lines.splitlines()]

nums.append(0)
nums.append(max(nums)+3)
nums = sorted(nums)

ones = 0
ths = 0
ways = [0] * len(nums)
ways[0] = 1
for i in range(1, len(nums)):
    if nums[i] - nums[i-1] == 1:
        ones += 1
    if nums[i] - nums[i-1] == 3:
        ths += 1
    if nums[i] - nums[i-1] <= 3:
        ways[i] += ways[i-1]
    if i > 1 and nums[i] - nums[i-2] <= 3:
        ways[i] += ways[i-2]
    if i > 2 and nums[i] - nums[i-3] <= 3:
        ways[i] += ways[i-3]

print(ones*ths)
print(ways[len(ways)-1])