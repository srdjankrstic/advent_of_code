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

DIR = {'R': 0, 'U': 1, 'L': 2, 'D': 3}

DIR8 = {'R': 0, 'D': 2, 'L': 4, 'U': 6}

def f1(lines):
    sol = 0
    head = lib.Point(0, 0)
    tail = lib.Point(0, 0)
    seen = set()
    for line in lines:
        [move, steps] = line.split(' ')
        steps = int(steps)
        d = DIR[move]
        for s in range(steps):
            seen.add((tail[0], tail[1]))
            head = lib.Point(head[0] + di[d], head[1] + dj[d])
            if tail.distance(head, norm=2) >= 2:
                tail = lib.Point(head[0] - di[d], head[1] - dj[d])
    sol = len(seen)
    return sol

def printrope(rope):
    for x in range(-10, 10):
        for y in range(-10, 10):
            for r in range(len(rope)):
                if x == rope[r][0] and y == rope[r][1]:
                    print(r, end='')
                    break
            else:
                print('.', end='')
        print()
    print()
    print()

def f2(lines):
    sol = 0
    moves = []
    for line in lines:
        [move, steps] = line.split(' ')
        for s in range(int(steps)):
            moves.append(DIR8[move])

    rope = [lib.Point(0, 0) for _ in range(10)]

    seen = set()
    for i, move in enumerate(moves):
        old_rope = deepcopy(rope)
        new_head = lib.Point(rope[0][0] + lib.di8[move], rope[0][1] + lib.dj8[move])
        rope[0] = new_head
        for knot in range(1, 10):
            dist = rope[knot].distance(rope[knot-1], norm=2)
            if dist == 2:
                px = -1 if rope[knot][0] - rope[knot - 1][0] > 0 else 1 if rope[knot][0] - rope[knot - 1][0] < 0 else 0
                py = -1 if rope[knot][1] - rope[knot - 1][1] > 0 else 1 if rope[knot][1] - rope[knot - 1][1] < 0 else 0
                rope[knot] = lib.Point(rope[knot][0] + px, rope[knot][1] + py)
            elif dist > 1.5:
                px = -1 if rope[knot][0] - rope[knot - 1][0] > 0 else 1
                py = -1 if rope[knot][1] - rope[knot - 1][1] > 0 else 1
                rope[knot] = lib.Point(rope[knot][0] + px, rope[knot][1] + py)

        seen.add((rope[9][0], rope[9][1]))
        # if i < 20:
        #     print(rope)
        #     printrope(rope)
    sol = len(seen)
    return sol


f = open(args.input, "r")
lines = [line for line in f.read().splitlines() if line.strip()]

if args.part == 1:
    print(f"solution: {f1(lines)}")
elif args.part == 2:
    print(f"solution: {f2(lines)}")
