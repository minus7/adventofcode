#!/usr/bin/env python3
# vim: set ts=4 sw=4 noet:

from itertools import combinations

with open("input") as f:
	data = [list(map(int, l.split("x"))) for l in f]


ribbon_required = 0
for package in data:
	perimeter = [2*(x+y) for x, y in combinations(package, 2)]
	volume = package[0] * package[1] * package[2]
	smallest = min(perimeter)
	# smallest perimeter + volume's number
	ribbon_required += smallest + volume

print(ribbon_required)
