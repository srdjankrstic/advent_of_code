import argparse
import re
from collections import defaultdict
import itertools as it
import math
from hashlib import md5
from advent_of_code import lib
from copy import deepcopy

di = lib.di4
dj = lib.dj4

parser = argparse.ArgumentParser()
parser.add_argument("input")
parser.add_argument("part", type=int)
args = parser.parse_args()

f = open(args.input, "r")
lines = [line for line in f.read().splitlines() if line.strip()]

def applymask(mask, val):
    m = len(mask)
    b = ['0'] * m
    z = list(lib.bin1(val))
    b [-len(z):] = z
    for i in range(m):
        if mask[m - i - 1] in "01":
            b[m - i - 1] = mask[m - i - 1]
    return int("".join(b), 2)

def apply2(mask, val):
    m = len(mask)
    b = ['0'] * m
    z = list(lib.bin1(val))
    b[-len(z):] = z
    for i in range(m):
        if mask[m - i - 1] in ("1", "a"):
            b[m - i - 1] = "1"
        if mask[m - i - 1] == "b":
            b[m - i - 1] = "0"
    zz = int("".join(b), 2)
    return zz

def pt2(mask, val):
    xs = [i for i, c in enumerate(mask) if c == 'X']
    sol = 0
    for i in range(-1, len(xs)):
        for p in it.combinations(xs, i+1):
            mask2 = deepcopy(mask)
            for pp in xs:
                if pp in p:
                    mask2[pp] = "a"
                else:
                    mask2[pp] = "b"
            yield apply2(mask2, val)

mem = {}
for li, line in enumerate(lines):
#    print(f"line {li}")    
    w = line.split(" ")
    if w[0] == "mask":
        mask = w[-1]
    else:
        [addr, val] = lib.rints(line)
        if args.part == 2:
            for s in pt2(list(mask), addr):
                mem[s] = val
        else:
            val = applymask(mask, val)
            mem[addr] = val

print(sum(mem.values()))
