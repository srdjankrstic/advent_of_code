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
import sympy.ntheory.factor_ as sf

di = lib.di4
dj = lib.dj4

parser = argparse.ArgumentParser()
parser.add_argument("input")
parser.add_argument("part", type=int)
args = parser.parse_args()

def total_size(cur, TOTAL_SIZES, raw_sizes):
    if cur in TOTAL_SIZES:
        return TOTAL_SIZES[cur]
    TOTAL_SIZES[cur] = raw_sizes[cur]
    for other_dir in raw_sizes.keys():
        if len(other_dir) > len(cur) and other_dir[:len(cur)] == cur and '/' not in other_dir[len(cur):len(other_dir)-1]:
            TOTAL_SIZES[cur] += total_size(other_dir, TOTAL_SIZES, raw_sizes)
    return TOTAL_SIZES[cur]

def f1():
    li = 0
    sizes = {}
    n = len(lines)
    cur_dir = '/'
    while True:
        if li >= n:
            break
        line = lines[li]
        if line[0] != '$':
            exit(1)
        words = line.split(' ')
        if words[1] == 'cd':
            if words[2] == '..':
                cur_dir = re.sub(r"/[^/]+/$", "/", cur_dir)
            elif words[2] == '/':
                cur_dir = '/'
            else:
                cur_dir += words[2] + '/'
            li += 1
        elif words[1] == 'ls':
            sizes[cur_dir] = 0
            while True:
                li += 1
                if li >= n:
                    break
                x = lines[li].split(' ')[0]
                if x == '$':
                    break
                if x =='dir':
                    continue
                sizes[cur_dir] += int(x)

    totals = {}
    total_size('/', totals, sizes)
    cutoff_sizes = [v for (k, v) in totals.items() if v <= 100000]
    return sum(cutoff_sizes)

def f2():
    li = 0
    sizes = {}
    n = len(lines)
    cur_dir = '/'
    while True:
        if li >= n:
            break
        line = lines[li]
        if line[0] != '$':
            exit(1)
        words = line.split(' ')
        if words[1] == 'cd':
            if words[2] == '..':
                cur_dir = re.sub(r"/[^/]+/$", "/", cur_dir)
            elif words[2] == '/':
                cur_dir = '/'
            else:
                cur_dir += words[2] + '/'
            li += 1
        elif words[1] == 'ls':
            sizes[cur_dir] = 0
            while True:
                li += 1
                if li >= n:
                    break
                x = lines[li].split(' ')[0]
                if x == '$':
                    break
                if x =='dir':
                    continue
                sizes[cur_dir] += int(x)

    totals = {}
    total_size('/', totals, sizes)
    needed = 30000000 - (70000000 - totals['/'])
    cutoff_sizes = [v for (k, v) in totals.items() if v >= needed]
    return min(cutoff_sizes)


f = open(args.input, "r")
lines = [line for line in f.read().splitlines() if line.strip()]

if args.part == 1:
    print(f"solution: {f1()}")
elif args.part == 2:
    print(f"solution: {f2()}")
