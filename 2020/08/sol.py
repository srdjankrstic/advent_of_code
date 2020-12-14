import argparse
import re
from collections import defaultdict

parser = argparse.ArgumentParser()
parser.add_argument("input")
parser.add_argument("part", type=int)
args = parser.parse_args()


def simulate(ops):
    n = len(ops)
    executed = [False] * n
    current = 0
    acc = 0
    count = 0
    while(True):
        if current == n:
            return True, acc
        if executed[current]:
            break
        executed[current] = True
        count += 1
        op = ops[current]
        if op[0] == "nop":
            current += 1
        if op[0] == "acc":
            current += 1
            acc += op[1]
        if op[0] == "jmp":
            current += op[1]

    return False, acc


f = open(args.input, "r")
contents = f.read()

ops = []
for line in contents.splitlines():
    m = re.match(r"^(...) (.)(\d+)$", line)
    num = int(m.group(3))
    if m.group(2) == "-":
        num = -num
    ops.append((m.group(1), num))

if args.part == 1:
    terminates, acc = simulate(ops)
    print(acc)
else:
    for i in range(len(ops)):
        if ops[i][0] == "jmp":
            ops[i] = ("nop", ops[i][1])
            terminates, acc = simulate(ops)
            if terminates:
                print(acc)
                exit(0)
            ops[i] = ("jmp", ops[i][1])
        elif ops[i][0] == "nop":
            ops[i] = ("jmp", ops[i][1])
            terminates, acc = simulate(ops)
            if terminates:
                print(acc)
                exit(0)
            ops[i] = ("nop", ops[i][1])
