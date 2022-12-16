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
    sol = 0
    tunnels = defaultdict(set)
    rtunnels = defaultdict(set)
    rates = defaultdict(int)
    for li, line in enumerate(lines):
        w = line.split(' ')
        v = w[1]
        rates[v] = lib.rints(line)[0]
        for dest in w[9:]:
            d = dest.replace(",", "")
            tunnels[v].add(d)
            rtunnels[d].add(v)
    valves = list(tunnels.keys())
    M = 30

    bests = [{v: {} for v in valves} for _ in range(M)]

    bests[0]['AA'][()] = 0
    for i in range(0, M-1):
        print(i)
        remaining = M - i - 1
        for v in valves:
            for state in bests[i][v]:
                if rates[v] and v not in state:
                    newstate = tuple(sorted(set(state).union({v})))
                    bests[i+1][v][newstate] = max(bests[i+1][v].get(newstate, 0), bests[i][v][state] + remaining * rates[v])
                for vp in tunnels[v]:
                    bests[i+1][vp][state] = max(bests[i+1][vp].get(state, 0), bests[i][v][state])
        for v in valves:
            del bests[i][v]
    for v in valves:
        sol = max(sol, max(bests[M-1][v].values()))
    return sol

def f2(data):
    lines = [line for line in data.splitlines() if line.strip()]
    sol = 0
    tunnels = defaultdict(set)
    rtunnels = defaultdict(set)
    rates = defaultdict(int)
    for li, line in enumerate(lines):
        w = line.split(' ')
        v = w[1]
        rates[v] = lib.rints(line)[0]
        for dest in w[9:]:
            d = dest.replace(",", "")
            tunnels[v].add(d)
            rtunnels[d].add(v)
    valves = list(tunnels.keys())
    M = 26

    bests = [{me: {el: {} for el in valves} for me in valves} for _ in range(M)]

    bests[0]['AA']['AA'][()] = 0

    for i in range(0, M-1):
        print(i)
        remaining = M - i - 1
        for me in valves:
            for el in valves:
                for state in bests[i][me][el]:
                    if me != el and rates[me] and rates[el] and me not in state and el not in state:
                        newstate = tuple(sorted(set(state).union({me, el})))
                        bests[i+1][me][el][newstate] = max(bests[i+1][me][el].get(newstate, 0), bests[i][me][el][state] + remaining * (rates[me] + rates[el]))
                    if rates[me] and me not in state:
                        newstate = tuple(sorted(set(state).union({me})))
                        for elp in tunnels[el]:
                            bests[i+1][me][elp][newstate] = max(bests[i+1][me][elp].get(newstate, 0), bests[i][me][el][state] + remaining * rates[me])
                    if rates[el] and el not in state:
                        newstate = tuple(sorted(set(state).union({el})))
                        for mep in tunnels[me]:
                            bests[i+1][mep][el][newstate] = max(bests[i+1][mep][el].get(newstate, 0), bests[i][me][el][state] + remaining * rates[el])
                    for mep in tunnels[me]:
                        for elp in tunnels[el]:
                            bests[i+1][mep][elp][state] = max(bests[i+1][mep][elp].get(state, 0), bests[i][me][el][state])
        for me in valves:
            for el in valves:
                del bests[i][me][el]
    for me in valves:
        for el in valves:
            sol = max(sol, max(bests[M-1][me][el].values()))
    return sol



f = open(args.input, "r")

if args.part == 1:
    print(f"solution: {f1(f.read())}")
elif args.part == 2:
    print(f"solution: {f2(f.read())}")
