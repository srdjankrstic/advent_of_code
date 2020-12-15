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
bak = deepcopy(lines)

regs = defaultdict(lambda: np.uint16(0))

def g(x):
    return np.uint16(int(x)) if lib.isint(x) else np.uint16(regs[x]) if x in regs else None

while(lines):
    for line in lines:
        [src, dst] = [x.strip() for x in line.split("->")]
        if "AND" in src:
            [r1, r2] = [g(x.strip()) for x in src.split("AND")]
            if r1 == None or r2 == None:
                continue
            regs[dst] = r1 & r2
            lines.remove(line)
        elif "OR" in src:
            [r1, r2] = [g(x.strip()) for x in src.split("OR")]
            if r1 == None or r2 == None:
                continue
            regs[dst] = r1 | r2
            lines.remove(line)
        elif "LSHIFT" in src:
            [r1, r2] = [g(x.strip()) for x in src.split("LSHIFT")]
            if r1 == None or r2 == None:
                continue
            regs[dst] = r1 << r2
            lines.remove(line)
        elif "RSHIFT" in src:
            [r1, r2] = [g(x.strip()) for x in src.split("RSHIFT")]
            if r1 == None or r2 == None:
                continue
            regs[dst] = r1 >> r2
            lines.remove(line)
        elif "NOT" in src:
            r1 = g(src.split(" ")[1])
            if r1 == None:
                continue
            regs[dst] = ~r1
            lines.remove(line)
        else:
            r1 = g(src)
            if r1 == None:
                continue
            regs[dst] = g(src)
            lines.remove(line)

print(regs['a'])
