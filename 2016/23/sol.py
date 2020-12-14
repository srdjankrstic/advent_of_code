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
regs['a'] = 7 if args.part == 1 else 12
zz = 0
while True:
    zz += 1
    if zz % 1000000 == 0:
        print(f"{zz}: {regs['a']}")
    if ptr >= len(inss):
        break
    x = inss[ptr]
    cmd = x[0]
    if cmd == "cpy":
        if len(x) == 3 and not lib.isint(x[2]):
            tar = x[2]
            src = x[1]
            if lib.isint(src):
                regs[tar] = int(src)
            else:
                regs[tar] = regs[src]
    elif cmd == "inc":
        if not lib.isint(x[1]):
            regs[x[1]] += 1
    elif cmd == "dec":
        if not lib.isint(x[1]):
            regs[x[1]] -= 1
    elif cmd == "jnz":
        off = int(x[2]) if lib.isint(x[2]) else regs[x[2]]
        val = int(x[1]) if lib.isint(x[1]) else regs[x[1]]
        if val != 0:
            ptr += off
            continue
    elif cmd == "tgl":
        off = int(x[1]) if lib.isint(x[1]) else regs[x[1]]
        tptr = ptr + off
        if tptr >= 0 and tptr < len(inss):
            if len(inss[tptr]) == 2:
                if inss[tptr][0] == "inc":
                    inss[tptr][0] = "dec"
                else:
                    inss[tptr][0] = "inc"
            else:
                if inss[tptr][0] == "jnz":
                    inss[tptr][0] = "cpy"
                else:
                    inss[tptr][0] = "jnz"

    ptr += 1
print(regs['a'])
