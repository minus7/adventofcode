#!/usr/bin/env python3
# vim: set ts=4 sw=4 noet:

from itertools import combinations
from collections import Counter

with open("input") as f:
	data = [l for l in f]


nice = 0
for s in data:
	# 2 equal letters, separated by one
	if not any(a==b for a, b in zip(s[:-2], s[2:])):
		continue

	pairs = [a+b for a, b in zip(s[:-1], s[1:])]
	i = 0
	while i < len(pairs)-1:
		if pairs[i] == pairs[i+1]:
			pairs.pop(i+1)
			continue
		i += 1
	if Counter(pairs).most_common(1)[0][1] > 1:
		nice += 1


print(nice)
