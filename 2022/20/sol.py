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

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class CircularLinkedList:  
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, val):
        n = Node(val)
        if not self.head:
            self.head = n
            self.tail = n
            self.head.next = self.head
            self.head.prev = self.head
            return
        n.prev = self.tail
        n.next = self.head
        self.tail.next = n
        self.head.prev = n
        self.tail = n

    def print(self):
        temp = self.head
        if self.head is not None:
            while(True):
                print(f"{temp.val} ", end="")
                temp = temp.next
                if (temp == self.head):
                    break
            print()

def f1(data):
    lines = [line for line in data.splitlines() if line.strip()]
    sol = 0
    cll = CircularLinkedList()
    for line in lines:
        cll.push(int(line))
    N = len(lines)
    moveorder = []
    cur = cll.head
    moveorder.append(cur)
    while cur != cll.tail:
        cur = cur.next
        moveorder.append(cur)

    for m in moveorder:
        if m.val % (N - 1) == 0:
            continue
        x = m
        y = m
        if m.val > 0:
            mv = m.val % (N - 1)
            for _ in range(mv):
                x = x.next
            # y = x.next
        if m.val < 0:
            mv = -m.val % (N - 1)
            for _ in range(mv + 1):
                x = x.prev
        y = x.next

        if m.next == x:
            x.next.prev = m
            m.prev.next = x
            x.prev = m.prev
            m.prev = x
            m.next = x.next
            x.next = m
        elif y.next == m:
            m.next.prev = y
            y.prev.next = m
            m.prev = y.prev
            y.prev = m
            y.next = m.next
            m.next = y
        else:
            m.prev.next = m.next
            m.next.prev = m.prev
            x.next = m
            y.prev = m
            m.next = y
            m.prev = x

        # cll.print()

    cur = cll.head
    while cur.val != 0:
        cur = cur.next
    cur1000 = cur
    cur2000 = cur
    cur3000 = cur

    for i in range(1000 % len(lines)):
        cur1000 = cur1000.next
    for i in range(2000 % len(lines)):
        cur2000 = cur2000.next
    for i in range(3000 % len(lines)):
        cur3000 = cur3000.next

    return cur1000.val + cur2000.val + cur3000.val

def f2(data):
    DKEY = 811589153
    lines = [line for line in data.splitlines() if line.strip()]
    sol = 0
    cll = CircularLinkedList()
    for line in lines:
        cll.push(int(line) * DKEY)
    N = len(lines)
    moveorder = []
    cur = cll.head
    moveorder.append(cur)
    while cur != cll.tail:
        cur = cur.next
        moveorder.append(cur)

    for z in range(10):
        for m in moveorder:
            if m.val % (N - 1) == 0:
                continue
            x = m
            y = m
            if m.val > 0:
                mv = m.val % (N - 1)
                for _ in range(mv):
                    x = x.next
                # y = x.next
            if m.val < 0:
                mv = -m.val % (N - 1)
                for _ in range(mv + 1):
                    x = x.prev
            y = x.next

            if m.next == x:
                x.next.prev = m
                m.prev.next = x
                x.prev = m.prev
                m.prev = x
                m.next = x.next
                x.next = m
            elif y.next == m:
                m.next.prev = y
                y.prev.next = m
                m.prev = y.prev
                y.prev = m
                y.next = m.next
                m.next = y
            else:
                m.prev.next = m.next
                m.next.prev = m.prev
                x.next = m
                y.prev = m
                m.next = y
                m.prev = x

        # cll.print()

    cur = cll.head
    while cur.val != 0:
        cur = cur.next
    cur1000 = cur
    cur2000 = cur
    cur3000 = cur

    for i in range(1000 % len(lines)):
        cur1000 = cur1000.next
    for i in range(2000 % len(lines)):
        cur2000 = cur2000.next
    for i in range(3000 % len(lines)):
        cur3000 = cur3000.next

    return cur1000.val + cur2000.val + cur3000.val



f = open(args.input, "r")

if args.part == 1:
    print(f"solution: {f1(f.read())}")
elif args.part == 2:
    print(f"solution: {f2(f.read())}")
