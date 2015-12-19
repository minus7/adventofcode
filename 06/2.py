#!/usr/bin/env python3
# vim: set ts=4 sw=4 noet:

from collections import namedtuple
import numpy as np

instructions = []
Cmd = namedtuple("Cmd", ("xs", "ys", "cmd"))
with open("input") as f:
	for l in f:
		rest, upper = l.split(" through ")
		upper = list(map(int, upper.split(",")))
		*rest, lower = rest.split(" ")
		lower = list(map(int, lower.split(",")))
		cmd = rest[-1]  # on/off/toggle
		instructions.append(Cmd(
			slice(lower[0], upper[0]+1),
			slice(lower[1], upper[1]+1),
			cmd
		))

grid = np.ndarray((1000, 1000), dtype=int)
grid.fill(0)

for cmd in instructions:
	if cmd.cmd == "toggle":
		grid[cmd.xs,cmd.ys] += 2
	else:
		grid[cmd.xs,cmd.ys] += 1 if cmd.cmd == "on" else -1
		np.clip(grid[cmd.xs,cmd.ys], 0, grid[cmd.xs,cmd.ys], out=grid[cmd.xs,cmd.ys])

print(np.sum(grid))
