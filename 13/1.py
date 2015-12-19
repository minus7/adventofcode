#!/usr/bin/env python3
# vim: set ts=4 sw=4 noet:

from itertools import permutations

people = set()
happiness_map = {}
with open("input") as f:
	for l in map(lambda x: x.strip().split(), f):
		a = l[0]
		b = l[-1][:-1]
		people.add(a)
		v = int(l[3])
		if l[2] == "lose":
			v = -v
		happiness_map[a, b] = v

max_happiness = 0
for perm in permutations(people):
	happiness = 0
	for l, p, r in zip(perm[-1:]+perm[:-1], perm, perm[1:]+perm[:1]):
		happiness += happiness_map[p, l] + happiness_map[p, r]
	if happiness > max_happiness:
		max_happiness = happiness

print(max_happiness)
