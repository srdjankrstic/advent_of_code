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


class OP:
    ADD = 1
    MULT = 2
    INPUT = 3
    OUTPUT = 4
    JNZ = 5
    JZ = 6
    LT = 7
    EQ = 8
    EXIT = 99

class Intcode:
    def __init__(self, inss, inp=None):
        self.inss = deepcopy(inss)
        self.ip = 0
        self.input = iter(inp) if type(inp) == tuple else iter((inp, ))
        self.output = None

    def decode(self):
        ins = f"{self.inss[self.ip]:>05}"
        self.opcode = int(ins[-2:])
        self.modes = [int(ins[2-i]) for i in range(0, 3)]

    def param(self, n):
        return self.inss[self.inss[self.ip + n]] if self.modes[n-1] == 0 else self.inss[self.ip + n]

    def apply(self):
        if self.opcode == OP.ADD:
            p1 = self.param(1)
            p2 = self.param(2)
            self.inss[self.inss[self.ip + 3]] = p1 + p2
            self.ip += 4
        elif self.opcode == OP.MULT:
            p1 = self.param(1)
            p2 = self.param(2)
            self.inss[self.inss[self.ip + 3]] = p1 * p2
            self.ip += 4
        elif self.opcode == OP.INPUT:
            self.inss[self.inss[self.ip + 1]] = next(self.input)
            self.ip += 2
        elif self.opcode == OP.OUTPUT:
            self.output = self.inss[self.inss[self.ip + 1]]
            self.ip += 2
        elif self.opcode == OP.JNZ:
            p1 = self.param(1)
            self.ip = self.ip + 3 if p1 == 0 else self.param(2)
        elif self.opcode == OP.JZ:
            p1 = self.param(1)
            self.ip = self.ip + 3 if p1 != 0 else self.param(2)
        elif self.opcode == OP.LT:
            p1 = self.param(1)
            p2 = self.param(2)
            self.inss[self.inss[self.ip + 3]] = 1 if p1 < p2 else 0
            self.ip += 4
        elif self.opcode == OP.EQ:
            p1 = self.param(1)
            p2 = self.param(2)
            self.inss[self.inss[self.ip + 3]] = 1 if p1 == p2 else 0
            self.ip += 4
        elif self.opcode == OP.EXIT:
            self.ip += 1
        else:
            exit()

    def exec(self):
        while True:
            self.decode()
            print(f"ip: {self.ip}, op: {self.opcode}")
            if self.opcode == OP.EXIT:
                return
            self.apply()


f = open(args.input, "r")
lines = [line for line in f.read().splitlines() if line.strip()]

for li, line in enumerate(lines):
    pass
