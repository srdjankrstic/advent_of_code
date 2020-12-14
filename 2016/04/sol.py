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

v = 0
for line in lines.splitlines():
    if not line:
        continue
    m = lib.rem(r"([a-z\-]+)-(\d+)\[(.*)\]", line)
    if not m:
        continue
    cnt = defaultdict(int)
    for c in m.group(1):
        if c != "-":
            cnt[c] += 1
    z = sorted(cnt.items(), key=lambda x: (-x[1], x[0]))
    chk = ""
    for i in range(5):
        chk += z[i][0]
    if m.group(3) == chk:
        v += int(m.group(2))
    if args.part == 2 and m.group(3) == chk:
        id = int(m.group(2))
        idm = id % 26
        print(f"{id} ", end="")
        for c in m.group(1):
            if c == "-":
                print(" ", end="")
            else:
                print(chr((ord(c) - ord('a') + idm) % 26 + ord('a')), end="")
        print("")

if args.part == 1:
    print(v)
