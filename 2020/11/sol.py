import argparse
import re
from collections import defaultdict
import itertools as it
import math
import copy

parser = argparse.ArgumentParser()
parser.add_argument("input")
parser.add_argument("part", type=int)
args = parser.parse_args()

f = open(args.input, "r")
lines = f.read()

def pgr(grid):
	for i in range(0, len(grid)):
		for j in range(0, len(grid[0])):
			print(grid[i][j], end="")
		print("")
	print("")

grid = []
i = 0
for line in lines.splitlines():
	grid.append([])
	if not line:
		continue
	for c in line:
		grid[i].append(c)
	i += 1

n = len(grid)
m = len(grid[0])
di = [-1, -1, -1, 0, 0, 1, 1, 1]
dj = [-1, 0, 1, -1, 1, -1, 0, 1]

if args.part == 1:
	while(True):
	#	pgr(grid)
		newgrid = copy.deepcopy(grid)
		ch = 0
		for i in range(0, len(grid)):
			for j in range(0, len(grid[0])):
				occ = 0 
				for d in range(8):
					pi = i + di[d]
					pj = j + dj[d]
					if pi < 0 or pi >= n or pj < 0 or pj >= m:
						continue
					if grid[pi][pj] == '#':
						occ += 1
				if grid[i][j] == 'L' and occ == 0:
					newgrid[i][j] = '#'
					ch += 1
				elif grid[i][j] == '#' and occ >= 5:
					newgrid[i][j] = 'L'
					ch += 1
				else:
					newgrid[i][j] = grid[i][j]
		grid = newgrid
		if ch == 0:
			break

if args.part == 2:
	while(True):
	#	pgr(grid)
		newgrid = copy.deepcopy(grid)
		ch = 0
		for i in range(0, len(grid)):
			for j in range(0, len(grid[0])):
				occ = 0

				pi = i - 1
				while pi >= 0 and grid[pi][j] == '.':
					pi -= 1
				if pi >= 0 and grid[pi][j] == '#':
					occ += 1

				pi = i + 1
				while pi < n and grid[pi][j] == '.':
					pi += 1
				if pi < n and grid[pi][j] == '#':
					occ += 1

				pj = j - 1
				while pj >= 0 and grid[i][pj] == '.':
					pj -= 1
				if pj >= 0 and grid[i][pj] == '#':
					occ += 1

				pj = j + 1
				while pj < m and grid[i][pj] == '.':
					pj += 1
				if pj < m and grid[i][pj] == '#':
					occ += 1

				pi = i - 1
				pj = j - 1
				while pi >= 0 and pj >= 0 and grid[pi][pj] == '.':
					pi -= 1
					pj -= 1
				if pi >= 0 and pj >= 0 and grid[pi][pj] == '#':
					occ += 1

				pi = i - 1
				pj = j + 1
				while pi >= 0 and pj < m and grid[pi][pj] == '.':
					pi -= 1
					pj += 1
				if pi >= 0 and pj < m and grid[pi][pj] == '#':
					occ += 1

				pi = i + 1
				pj = j - 1
				while pi < n and pj >= 0 and grid[pi][pj] == '.':
					pi += 1
					pj -= 1
				if pi < n and pj >= 0 and grid[pi][pj] == '#':
					occ += 1

				pi = i + 1
				pj = j + 1
				while pi < n and pj < m and grid[pi][pj] == '.':
					pi += 1
					pj += 1
				if pi < n and pj < m and grid[pi][pj] == '#':
					occ += 1

				if grid[i][j] == 'L' and occ == 0:
					newgrid[i][j] = '#'
					ch += 1
				elif grid[i][j] == '#' and occ >= 5:
					newgrid[i][j] = 'L'
					ch += 1
				else:
					newgrid[i][j] = grid[i][j]
		grid = newgrid
		if ch == 0:
			break

tot = 0
for i in range(0, len(grid)):
	for j in range(0, len(grid[0])):
		if grid[i][j] == '#':
			tot += 1
print(tot)

