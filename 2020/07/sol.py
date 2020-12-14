import argparse
import re
from collections import defaultdict

parser = argparse.ArgumentParser()
parser.add_argument("input")
parser.add_argument("part", type=int)
args = parser.parse_args()

f = open(args.input, "r")
contents = f.read()

sol = 0
paths = defaultdict(list)
revpath = defaultdict(list)
for line in contents.splitlines():
    m1 = re.match(r"^(.*) bags contain (.*)\.$", line)
    outer = m1.group(1)
    rules = line.split(',')
    rules[0] = rules[0][len(outer) + len(" bags contain"):]
    for rule in rules:
        m = re.match(r" (\d+)+ (.*) bags?\.?$", rule)
        if not m:
            continue
        cnt = int(m.group(1))
        col = m.group(2)
        paths[col].append(outer)
        revpath[outer].append((col, cnt))

    q = ["shiny gold"]
    reachable = set()
    while(True):
        x = q[0]
        q.pop(0)
        for y in paths[x]:
            if y not in reachable:
                reachable.add(y)
                q.append(y)
        if len(q) == 0:
            break

    total = 0
    q = [("shiny gold", 1)]
    while(True):
        (x, mult) = q[0]
        q.pop(0)
        for tpl in revpath[x]:
            total += mult * tpl[1]
            q.append((tpl[0], mult * tpl[1]))
        if len(q) == 0:
            break

print(len(reachable))
print(total)
