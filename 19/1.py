#!/usr/bin/env python3
# vim: set ts=4 sw=4 noet:

from collections import defaultdict

replacements = defaultdict(list)
with open("input") as f:
	for l in map(str.strip, f):
		if not l:
			break
		a, b = l.split(" => ")
		replacements[a].append(b)
	start = f.readline().strip()

possible = set()
for a, reps in replacements.items():
	for rep in reps:
		parts = start.split(a)
		for i in range(1, len(parts)):
			new = a.join(parts[0:i]) + rep + a.join(parts[i:])
			possible.add(new)

print(len(possible))
