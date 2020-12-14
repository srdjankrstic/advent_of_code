import argparse
import re

parser = argparse.ArgumentParser()
parser.add_argument("input")
parser.add_argument("part", type=int)
args = parser.parse_args()

f = open(args.input, "r")
contents = f.read()

seen = dict()
lines = 0
total = 0
totalall = 0
for line in contents.splitlines():
    if not line:
        total += len(seen)
        totalall += len([x for x in seen.values() if x == lines])
        seen = dict()
        lines = 0
        continue
    lines += 1
    for c in line:
        if c not in seen:
            seen[c] = 1
        else:
            seen[c] += 1

total += len(seen)
totalall += len([x for x in seen.values() if x == lines])
print(total)
print(totalall)
