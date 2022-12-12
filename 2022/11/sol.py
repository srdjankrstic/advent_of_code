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

def f1():
    monkeycommands = []
    monkeylines = f.read().split('\n\n')
    for m in monkeylines:
        monkeycommands.append([l.strip() for l in m.split("\n")])
    monkeys = []
    
    for mc in monkeycommands:
        monkey = defaultdict()
        monkey['items'] = lib.rints(mc[1])
        monkey['op'] = mc[2].split(' ')[-2]
        monkey['op1'] = mc[2].split(' ')[-3]
        monkey['op2'] = mc[2].split(' ')[-1]
        monkey['test'] = int(mc[3].split(' ')[-1])
        monkey['true'] = int(mc[4].split(' ')[-1])
        monkey['false'] = int(mc[5].split(' ')[-1])
        monkey['inspections'] = 0
        monkeys.append(monkey)


    ROUNDS = 20
    for r in range(ROUNDS):
        for m in monkeys:
            mcp = deepcopy(m['items'])
            for mi in mcp:
                m['inspections'] += 1
                m['items'].pop(0)
                op1 = mi if m['op1'] == 'old' else int(m['op1'])
                op2 = mi if m['op2'] == 'old' else int(m['op2'])
                mi = op1 + op2 if m['op'] == '+' else op1 * op2
                mi //= 3
                if mi % m['test'] == 0:
                    monkeys[m['true']]['items'].append(mi)
                else:
                    monkeys[m['false']]['items'].append(mi)

    monkeys = sorted(monkeys, key=lambda m: -m['inspections'])
    return monkeys[0]['inspections'] * monkeys[1]['inspections']

def f2():
    monkeycommands = []
    monkeylines = f.read().split('\n\n')
    for m in monkeylines:
        monkeycommands.append([l.strip() for l in m.split("\n")])
    monkeys = []
    
    for mc in monkeycommands:
        monkey = defaultdict()
        monkey['items'] = lib.rints(mc[1])
        monkey['op'] = mc[2].split(' ')[-2]
        monkey['op1'] = mc[2].split(' ')[-3]
        monkey['op2'] = mc[2].split(' ')[-1]
        monkey['test'] = int(mc[3].split(' ')[-1])
        monkey['true'] = int(mc[4].split(' ')[-1])
        monkey['false'] = int(mc[5].split(' ')[-1])
        monkey['inspections'] = 0
        monkeys.append(monkey)

    lcm = lib.lcm(*[m['test'] for m in monkeys])

    ROUNDS = 10000
    for r in range(ROUNDS):
        for m in monkeys:
            mcp = deepcopy(m['items'])
            for mi in mcp:
                m['inspections'] += 1
                m['items'].pop(0)
                op1 = mi if m['op1'] == 'old' else int(m['op1'])
                op2 = mi if m['op2'] == 'old' else int(m['op2'])
                mi = op1 + op2 if m['op'] == '+' else op1 * op2
                # mi //= 3
                mi %= lcm
                if mi % m['test'] == 0:
                    monkeys[m['true']]['items'].append(mi)
                else:
                    monkeys[m['false']]['items'].append(mi)

    monkeys = sorted(monkeys, key=lambda m: -m['inspections'])
    return monkeys[0]['inspections'] * monkeys[1]['inspections']

f = open(args.input, "r")

if args.part == 1:
    print(f"solution: {f1()}")
elif args.part == 2:
    print(f"solution: {f2()}")
