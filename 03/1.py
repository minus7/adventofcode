#!/usr/bin/env python3
# vim: set ts=4 sw=4 noet:

from collections import namedtuple, defaultdict

with open("input") as f:
	data = f.read()

class Pos:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def go(self, c):
		if c == "^":
			self.y -= 1
		elif c == "v":
			self.y += 1
		elif c == "<":
			self.x -= 1
		elif c == ">":
			self.x += 1
		else:
			raise ValueError("unexpected token {}".format(c))
	
	def tuple(self):
		return self.x, self.y

grid = defaultdict(int)

pos = Pos(0, 0)

grid[pos.tuple()] = 1

for c in data:
	pos.go(c)
	grid[pos.tuple()] += 1

print(len(grid))
