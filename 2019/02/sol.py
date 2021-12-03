import argparse
import re
from collections import defaultdict
from functools import reduce
import itertools as it
import math
from hashlib import md5
from advent_of_code import lib
from copy import deepcopy
import numpy as np
import json
import sympy.ntheory.factor_

di = lib.di4
dj = lib.dj4

parser = argparse.ArgumentParser()
parser.add_argument("input")
parser.add_argument("part", type=int)
args = parser.parse_args()

f = open(args.input, "r")
lines = [line for line in f.read().splitlines() if line.strip()]

def run(pos):
    cur = 0
    while True:
        if pos[cur] == 99:
            return
        elif pos[cur] == 1:
            pos[pos[cur + 3]] = pos[pos[cur + 1]] + pos[pos[cur + 2]]
        elif pos[cur] == 2:
            pos[pos[cur + 3]] = pos[pos[cur + 1]] * pos[pos[cur + 2]]
        cur += 4

for li, line in enumerate(lines):
    pos = lib.rints(line)
    if args.part == 1:
        run(pos)
        print(pos[0])
    else:
        for noun in range(100):
            for verb in range(100):
                ppos = deepcopy(pos)
                ppos[1] = noun
                ppos[2] = verb
                run(ppos)
                if ppos[0] == 19690720:
                    print(100*noun+verb)
