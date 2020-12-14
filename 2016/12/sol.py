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

regs = defaultdict(int)
inss = []
for li, line in enumerate(lines):
    inss.append(line.split(" "))

ptr = 0
if args.part == 2:
    regs['c'] = 1
while True:
    if ptr >= len(inss):
        break
    x = inss[ptr]
    cmd = x[0]
    if cmd == "cpy":
        tar = x[2]
        src = x[1]
        if lib.isint(src):
            regs[tar] = int(src)
        else:
            regs[tar] = regs[src]
    elif cmd == "inc":
        regs[x[1]] += 1
    elif cmd == "dec":
        regs[x[1]] -= 1

    elif cmd == "jnz":
        val = int(x[1]) if lib.isint(x[1]) else regs[x[1]]
        if val != 0:
            ptr += int(x[2])
            continue
    ptr += 1
print(regs['a'])
