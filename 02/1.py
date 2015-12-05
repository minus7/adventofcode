#!/usr/bin/env python3
# vim: set ts=4 sw=4 noet:

from itertools import combinations

with open("input") as f:
	data = [l.split("x") for l in f]


paper_required = 0
for package in data:
	sides = [x*y for x, y in combinations(map(int, package), 2)]
	smallest = min(sides)
	# paper for all 6 sides plus extra
	paper_required += sum(sides)*2 + smallest

print(paper_required)
