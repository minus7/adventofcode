#!/usr/bin/env python3
# vim: set ts=4 sw=4 noet:

from itertools import combinations

with open("input") as f:
	data = [l for l in f]


nice = 0
for s in data:
	vowels = 0
	twice = False
	prev = None
	if any(naughty in s for naughty in ("ab", "cd", "pq", "xy")):
		continue
	for c in s:
		if c in "aeiou":
			vowels += 1
		if prev == c:
			twice = True
		prev = c
	if twice and vowels >= 3:
		nice += 1



print(nice)
