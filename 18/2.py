#!/usr/bin/env python3
# vim: set ts=4 sw=4 noet:

import numpy as np

grid = []
with open("input") as f:
	for l in map(str.strip, f):
		grid.append(list(c == "#" for c in l))

grid = np.array(grid)
grid[0, 0] = True
grid[-1, 0] = True
grid[-1, -1] = True
grid[0, -1] = True

sy, sx = grid.shape

def print_grid():
	print("\n".join("".join("#" if c else "." for c in r) for r in grid))

def neighbour_sum(y, x):
	minx = max(x-1, 0)
	miny = max(y-1, 0)
	maxx = min(x+1, sx)+1
	maxy = min(y+1, sy)+1
	return np.sum(grid[miny:maxy, minx:maxx]) - int(grid[y, x])

for turn in range(100):
	new_grid = grid.copy()
	for y in range(sy):
		for x in range(sx):
			if grid[y, x] and not (2 <= neighbour_sum(y, x) <= 3):
				new_grid[y, x] = False
			elif not grid[y, x] and neighbour_sum(y, x) == 3:
				new_grid[y, x] = True
	new_grid[0, 0] = True
	new_grid[-1, 0] = True
	new_grid[-1, -1] = True
	new_grid[0, -1] = True
	grid = new_grid
	#print_grid()

print(np.sum(grid))
