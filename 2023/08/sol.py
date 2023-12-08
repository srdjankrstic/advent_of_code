import argparse
import re
from collections import defaultdict
from functools import reduce, cmp_to_key
import itertools as it
import math
from hashlib import md5
from advent_of_code import lib
from copy import deepcopy
import numpy as np
import json
import sympy.ntheory.factor_ as sf

di = lib.di4
dj = lib.dj4

parser = argparse.ArgumentParser()
parser.add_argument("input")
parser.add_argument("part", type=int)
args = parser.parse_args()

def f1(data):
    lines = [line for line in data.splitlines() if line.strip()]
    instructions = lines[0]
    data = defaultdict(tuple)
    sol = 0
    for li, line in enumerate(lines[1:]):
        data[line[0:3]] = (line[7:10], line[12:15])
    current = 'AAA'
    while current != 'ZZZ':
        instr = instructions[sol % len(instructions)]
        current = data[current][0] if instr == 'L' else data[current][1]
        sol += 1
    return sol

def f2(data):
    lines = [line for line in data.splitlines() if line.strip()]
    instructions = lines[0]
    data = defaultdict(tuple)
    sol = 0
    for li, line in enumerate(lines[1:]):
        data[line[0:3]] = (line[7:10], line[12:15])
    zs = []
    for s in [k for k in data.keys() if k[-1] == 'A']:
        i = 0
        current = s
        while True:
            if current[-1] == 'Z':
                zs.append(i)
                break
            instr = instructions[i % len(instructions)]
            i += 1
            current = data[current][0] if instr == 'L' else data[current][1]
    return lib.lcm(*zs)


f = open(args.input, "r")

if args.part == 1:
    print(f"solution: {f1(f.read())}")
elif args.part == 2:
    print(f"solution: {f2(f.read())}")
