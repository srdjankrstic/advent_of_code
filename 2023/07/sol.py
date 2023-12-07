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

CARDS = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'J': 11,
    'T': 10,
    '9': 9,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3,
    '2': 2,
}
CARDS2 = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'T': 10,
    '9': 9,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3,
    '2': 2,
    'J': 1,
}
REVCARDS = {v: k for k, v in CARDS.items()}

def value(hand):
    themap = defaultdict(int)
    for c in hand:
        themap[CARDS[c]] += 1
    counts = sorted(themap.values())
    tier = 0
    if counts == [5]:
        tier = 6
    elif counts == [1, 4]:
        tier = 5
    elif counts == [2, 3]:
        tier = 4
    elif 3 in counts:
        tier = 3
    elif counts == [1, 2, 2]:
        tier = 2
    elif 2 in counts:
        tier = 1
    return (tier, [CARDS[c] for c in hand])

def value2(hand):
    best = 0
    if 'J' in hand:
        x = hand.index('J')
        for joker in range(2, 15):
            if joker == 11:
                continue
            newhand = f"{hand[0:x]}{REVCARDS[joker]}{hand[x+1:]}"
            (newvalue, _) = value2(newhand)
            best = max(best, newvalue)
        return (best, [CARDS2[c] for c in hand])
    return value(hand)

def f1(data):
    lines = [line for line in data.splitlines() if line.strip()]
    sol = 0
    handbids = []
    for li, line in enumerate(lines):
        [hand, bid] = line.split(" ")
        handbids.append((value(hand), int(bid)))
    handbids = sorted(handbids)
    for i in range(len(handbids)):
        sol += (i + 1) * handbids[i][1]
    return sol

def f2(data):
    lines = [line for line in data.splitlines() if line.strip()]
    sol = 0
    handbids = []
    for li, line in enumerate(lines):
        [hand, bid] = line.split(" ")
        handbids.append((value2(hand), int(bid)))
    handbids = sorted(handbids)
    for i in range(len(handbids)):
        # print(handbids[i])
        sol += (i + 1) * handbids[i][1]
    return sol

f = open(args.input, "r")

if args.part == 1:
    print(f"solution: {f1(f.read())}")
elif args.part == 2:
    print(f"solution: {f2(f.read())}")
