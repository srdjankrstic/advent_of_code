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
    n = len(lines)
    grid = defaultdict(str)
    graph = defaultdict(list)
    s = lib.Point(0, 0)
    for li, line in enumerate(lines):
        for i, c in enumerate(line):
            this = lib.Point(li, i)
            grid[this] = c
            if c == "S":
                s = this
    for i in range(n):
        for j in range(n):
            this = lib.Point(i, j)
            c = grid[this]
            if c == "|":
                if i > 0 and grid[lib.Point(i - 1, j)] in ['|', '7', 'F', 'S']:
                    graph[this].append(lib.Point(i - 1, j))
                if i < n - 1 and grid[lib.Point(i + 1, j)] in ['|', 'L', 'J', 'S']:
                    graph[this].append(lib.Point(i + 1, j))
            if c == "-":
                if j > 0 and grid[lib.Point(i, j - 1)] in ['-', 'L', 'F', 'S']:
                    graph[this].append(lib.Point(i, j - 1))
                if j < n - 1 and grid[lib.Point(i, j + 1)] in ['-', 'J', '7', 'S']:
                    graph[this].append(lib.Point(i, j + 1))
            if c == "L":
                if i > 0 and grid[lib.Point(i - 1, j)] in ['|', '7', 'F', 'S']:
                    graph[this].append(lib.Point(i - 1, j))
                if j < n - 1 and grid[lib.Point(i, j + 1)] in ['-', 'J', '7', 'S']:
                    graph[this].append(lib.Point(i, j + 1))
            if c == "J":
                if i > 0 and grid[lib.Point(i - 1, j)] in ['|', '7', 'F', 'S']:
                    graph[this].append(lib.Point(i - 1, j))
                if j > 0 and grid[lib.Point(i, j - 1)] in ['-', 'L', 'F', 'S']:
                    graph[this].append(lib.Point(i, j - 1))
            if c == "7":
                if j > 0 and grid[lib.Point(i, j - 1)] in ['-', 'L', 'F', 'S']:
                    graph[this].append(lib.Point(i, j - 1))
                if i < n - 1 and grid[lib.Point(i + 1, j)] in ['|', 'L', 'J', 'S']:
                    graph[this].append(lib.Point(i + 1, j))
            if c == "F":
                if i < n - 1 and grid[lib.Point(i + 1, j)] in ['|', 'L', 'J', 'S']:
                    graph[this].append(lib.Point(i + 1, j))
                if j < n - 1 and grid[lib.Point(i, j + 1)] in ['-', 'J', '7', 'S']:
                    graph[this].append(lib.Point(i, j + 1))
            if c == "S":
                if i > 0 and grid[lib.Point(i - 1, j)] in ['|', '7', 'F', 'S']:
                    graph[this].append(lib.Point(i - 1, j))
                if i < n - 1 and grid[lib.Point(i + 1, j)] in ['|', 'L', 'J', 'S']:
                    graph[this].append(lib.Point(i + 1, j))
                if j > 0 and grid[lib.Point(i, j - 1)] in ['-', 'L', 'F', 'S']:
                    graph[this].append(lib.Point(i, j - 1))
                if j < n - 1 and grid[lib.Point(i, j + 1)] in ['-', 'J', '7', 'S']:
                    graph[this].append(lib.Point(i, j + 1))

    visited = set([s])
    q = [s]
    distances = defaultdict(int)
    distances[s] = 0
    maxdist = 0
    while len(q):
        p = q.pop(0)
        for new in graph[p]:
            if new not in visited:
                visited.add(new)
                q.append(new)
                distances[new] = distances[p] + 1
                maxdist = max(maxdist, distances[new])
    return maxdist

def f2(data):
    lines = [line for line in data.splitlines() if line.strip()]
    n = len(lines)
    grid = defaultdict(str)
    graph = defaultdict(list)
    s = lib.Point(0, 0)
    for li, line in enumerate(lines):
        for i, c in enumerate(line):
            if c == 'S':
                c = '|'  # yea yea
                s = lib.Point(3*li+1, 3*i+1)
            grid[lib.Point(3*li, 3*i)] = '.'
            grid[lib.Point(3*li, 3*i+2)] = '.'
            grid[lib.Point(3*li+2, 3*i)] = '.'
            grid[lib.Point(3*li+2, 3*i+2)] = '.'
            grid[lib.Point(3*li+1, 3*i+1)] = c
            if c == '|':
                grid[lib.Point(3*li, 3*i+1)] = '|'
                grid[lib.Point(3*li+2, 3*i+1)] = '|'
                grid[lib.Point(3*li+1, 3*i)] = '.'
                grid[lib.Point(3*li+1, 3*i+2)] = '.'
            elif c == '-':
                grid[lib.Point(3*li, 3*i+1)] = '.'
                grid[lib.Point(3*li+2, 3*i+1)] = '.'
                grid[lib.Point(3*li+1, 3*i)] = '-'
                grid[lib.Point(3*li+1, 3*i+2)] = '-'
            elif c == 'L':
                grid[lib.Point(3*li, 3*i+1)] = '|'
                grid[lib.Point(3*li+2, 3*i+1)] = '.'
                grid[lib.Point(3*li+1, 3*i)] = '.'
                grid[lib.Point(3*li+1, 3*i+2)] = '-'
            elif c == 'J':
                grid[lib.Point(3*li, 3*i+1)] = '|'
                grid[lib.Point(3*li+2, 3*i+1)] = '.'
                grid[lib.Point(3*li+1, 3*i)] = '-'
                grid[lib.Point(3*li+1, 3*i+2)] = '.'
            elif c == '7':
                grid[lib.Point(3*li, 3*i+1)] = '.'
                grid[lib.Point(3*li+2, 3*i+1)] = '|'
                grid[lib.Point(3*li+1, 3*i)] = '-'
                grid[lib.Point(3*li+1, 3*i+2)] = '.'
            elif c == 'F':
                grid[lib.Point(3*li, 3*i+1)] = '.'
                grid[lib.Point(3*li+2, 3*i+1)] = '|'
                grid[lib.Point(3*li+1, 3*i)] = '.'
                grid[lib.Point(3*li+1, 3*i+2)] = '-'
            else:
                grid[lib.Point(3*li, 3*i+1)] = '.'
                grid[lib.Point(3*li+2, 3*i+1)] = '.'
                grid[lib.Point(3*li+1, 3*i)] = '.'
                grid[lib.Point(3*li+1, 3*i+2)] = '.'
    n *= 3
    for i in range(n):
        for j in range(n):
            this = lib.Point(i, j)
            c = grid[this]
            if c == "|":
                if i > 0 and grid[lib.Point(i - 1, j)] in ['|', '7', 'F', 'S']:
                    graph[this].append(lib.Point(i - 1, j))
                if i < n - 1 and grid[lib.Point(i + 1, j)] in ['|', 'L', 'J', 'S']:
                    graph[this].append(lib.Point(i + 1, j))
            if c == "-":
                if j > 0 and grid[lib.Point(i, j - 1)] in ['-', 'L', 'F', 'S']:
                    graph[this].append(lib.Point(i, j - 1))
                if j < n - 1 and grid[lib.Point(i, j + 1)] in ['-', 'J', '7', 'S']:
                    graph[this].append(lib.Point(i, j + 1))
            if c == "L":
                if i > 0 and grid[lib.Point(i - 1, j)] in ['|', '7', 'F', 'S']:
                    graph[this].append(lib.Point(i - 1, j))
                if j < n - 1 and grid[lib.Point(i, j + 1)] in ['-', 'J', '7', 'S']:
                    graph[this].append(lib.Point(i, j + 1))
            if c == "J":
                if i > 0 and grid[lib.Point(i - 1, j)] in ['|', '7', 'F', 'S']:
                    graph[this].append(lib.Point(i - 1, j))
                if j > 0 and grid[lib.Point(i, j - 1)] in ['-', 'L', 'F', 'S']:
                    graph[this].append(lib.Point(i, j - 1))
            if c == "7":
                if j > 0 and grid[lib.Point(i, j - 1)] in ['-', 'L', 'F', 'S']:
                    graph[this].append(lib.Point(i, j - 1))
                if i < n - 1 and grid[lib.Point(i + 1, j)] in ['|', 'L', 'J', 'S']:
                    graph[this].append(lib.Point(i + 1, j))
            if c == "F":
                if i < n - 1 and grid[lib.Point(i + 1, j)] in ['|', 'L', 'J', 'S']:
                    graph[this].append(lib.Point(i + 1, j))
                if j < n - 1 and grid[lib.Point(i, j + 1)] in ['-', 'J', '7', 'S']:
                    graph[this].append(lib.Point(i, j + 1))
            if c == "S":
                if i > 0 and grid[lib.Point(i - 1, j)] in ['|', '7', 'F', 'S']:
                    graph[this].append(lib.Point(i - 1, j))
                if i < n - 1 and grid[lib.Point(i + 1, j)] in ['|', 'L', 'J', 'S']:
                    graph[this].append(lib.Point(i + 1, j))
                if j > 0 and grid[lib.Point(i, j - 1)] in ['-', 'L', 'F', 'S']:
                    graph[this].append(lib.Point(i, j - 1))
                if j < n - 1 and grid[lib.Point(i, j + 1)] in ['-', 'J', '7', 'S']:
                    graph[this].append(lib.Point(i, j + 1))

    visited = set([s])
    q = [s]
    distances = defaultdict(int)
    distances[s] = 0
    maxdist = 0
    maxdistp = s
    while len(q):
        p = q.pop(0)
        for new in graph[p]:
            if new not in visited:
                visited.add(new)
                q.append(new)
                distances[new] = distances[p] + 1
                maxdist = max(maxdist, distances[new])
                maxdistp = new

    longest_loop = set([maxdistp])
    cur = maxdistp
    while True:
        found = False
        for new in graph[cur]:
            if new not in longest_loop:
                longest_loop.add(new)
                cur = new
                found = True
                break
        if not found:
            break
    longest_loop.add(s)

    rooms = defaultdict(int)
    curroom = 0
    visited = set()
    notit = set()
    for i in range(n):
        for j in range(n):
            this = lib.Point(i, j)
            if this not in visited and this not in longest_loop:
                curroom += 1
                q = [this]
                visited.add(this)
                rooms[this] = curroom
                while len(q):
                    p = q.pop(0)
                    for newp in p.neigh_l1():
                        if newp in longest_loop:
                            continue
                        if newp in visited:
                            if rooms[newp] != curroom:
                                notit.add(curroom)
                            continue
                        if newp[0] < 0 or newp[0] >= n or newp[1] < 0 or newp[1] >= n:
                            notit.add(curroom)
                            continue
                        visited.add(newp)
                        q.append(newp)
                        rooms[newp] = curroom

    # for i in range(n):
    #     for j in range(n):
    #         this = lib.Point(i, j)
    #         if this not in longest_loop:
    #             print(f"{rooms[this]:3}", end='')
    #         else:
    #             print(f"{grid[this]:3}", end='')
    #     print("")

    sol = 0
    goodrooms = set(rooms.values()) - notit

    for p in rooms:
        if p[0] % 3 == 1 and p[1] % 3 == 1 and rooms[p] in goodrooms:
            sol += 1
    return sol


f = open(args.input, "r")

if args.part == 1:
    print(f"solution: {f1(f.read())}")
elif args.part == 2:
    print(f"solution: {f2(f.read())}")
