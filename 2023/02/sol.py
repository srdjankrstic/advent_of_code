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

red = 12
green = 13
blue = 14

def f1(data):
    lines = [line for line in data.splitlines() if line.strip()]
    sol = 0
    for li, line in enumerate(lines):
        [game, line] = line.split(':')
        gamenum = lib.rints(game)[0]
        x = line.split(';')
        possible = True
        for part in x:
            for y in part.split(','):
                n = lib.rints(y)[0]
                if ('red' in y and n > red) or ('blue' in y and n > blue) or ('green' in y and n > green):
                    possible = False
                    break
        if possible:
            sol += gamenum
    return sol

def f2(data):
    lines = [line for line in data.splitlines() if line.strip()]
    sol = 0
    for li, line in enumerate(lines):
        [game, line] = line.split(':')
        gamenum = lib.rints(game)[0]
        x = line.split(';')
        minred = minxgreen = minblue = 0
        for part in x:
            for y in part.split(','):
                n = lib.rints(y)[0]
                if 'red' in y:
                    minred = max(minred, n)
                if 'blue' in y:
                    minblue = max(minblue, n)
                if 'green' in y:
                    minxgreen = max(minxgreen, n)
        sol += minred * minblue * minxgreen
    return sol


f = open(args.input, "r")

if args.part == 1:
    print(f"solution: {f1(f.read())}")
elif args.part == 2:
    print(f"solution: {f2(f.read())}")
