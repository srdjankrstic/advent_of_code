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

for i in it.count(0):
    regs = dict()
    regs['a'] = i
    ptr = 0
    signal = []

    print(f"Trying {i}:")
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
        elif cmd == "out":
            signal.append(regs[x[1]])
            if len(signal) > 1 and not ((signal[-2] == 0 and signal[-1] == 1) or (signal[-2] == 1 and signal[-1] == 0)):
                break
        ptr += 1
