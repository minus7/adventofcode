#!/usr/bin/env python3
# vim: set ts=4 sw=4 noet:

from collections import defaultdict
from itertools import count

replacements = defaultdict(list)
with open("input") as f:
	for l in map(str.strip, f):
		if not l:
			break
		a, b = l.split(" => ")
		replacements[a].append(b)
	end = f.readline().strip()

min_depth = 999999999
def search(start, depth=1):
	global min_depth
	for a, reps in replacements.items():
		for rep in reps:
			parts = start.split(rep)
			for i in range(1, len(parts)):
				new = rep.join(parts[0:i]) + a + rep.join(parts[i:])
				if new == "e":
					if depth < min_depth:
						min_depth = depth
						print(min_depth)
					return
				search(new, depth+1)

search(end)
print(min_depth)
