#!/usr/bin/env python3
# vim: set ts=4 sw=4 noet:

from itertools import permutations

locs = []
locs_int = []
def map_loc(loc):
	if loc in locs:
		return 1 << locs.index(loc)
	locs.append(loc)
	locs_int.append(1 << (len(locs)-1))
	return locs_int[-1]

distances = {}
with open("input") as f:
	for l in map(lambda x: x.strip().split(), f):
		a = map_loc(l[0])
		b = map_loc(l[2])
		v = int(l[4])
		distances[a | b] = v

max_dist = 0
for perm in permutations(locs_int):
	dist = 0
	for a, b in zip(perm[:-1], perm[1:]):
		dist += distances[a | b]
	if dist > max_dist:
		max_dist = dist
		max_path = perm

print(max_dist)
