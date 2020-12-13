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

if args.part == 1:
    for li, line in enumerate(lines):
        if li == 0:
            start = int(line)
        ts = lib.rints(line)

    for i in it.count(start + 1):
        for t in ts:
            if i % t == 0:
                print((i - start) * t)
                exit(0)
elif args.part == 2:
    start = 100000000000000
    jump = 1
    off = 0
    z = []
    for li, line in enumerate(lines):
        if li == 0:
            continue
        for i, n in enumerate(line.split(",")):
            if n != 'x':
                z.append((i, int(n)))
    z = sorted(z, key=lambda x: (x[1], x[0]))
    while True:
        for t in it.count(start, jump):
            if (t + z[off][0]) % z[off][1] == 0:
                jump = lib.lcm(jump, z[off][1])
                start = t
                off += 1
                break
        if off == len(z):
            print(start)
            exit(0)
