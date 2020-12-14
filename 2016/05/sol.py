import argparse
import re
from collections import defaultdict
import itertools as it
import math
from hashlib import md5
from advent_of_code import lib


parser = argparse.ArgumentParser()
parser.add_argument("input")
parser.add_argument("part", type=int)
args = parser.parse_args()

f = open(args.input, "r")
lines = f.read()

for line in lines.splitlines():
    if not line:
        continue
    sol = [] if args.part == 1 else ["_"] * 8
    for i in it.count():
        x = line + str(i)
        h = md5(x.encode('utf-8')).hexdigest()
        if h[:5] == "00000":
            if args.part == 1:
                print(i)
                sol.append(h[5])
                if len(sol) == 8:
                    break
            else:
                pos = int(h[5], base=16)
                if pos > 7 or sol[pos] != "_":
                    continue
                sol[pos] = h[6]
                if "_" not in sol:
                    break
                print("".join(sol))
    print("".join(sol))
