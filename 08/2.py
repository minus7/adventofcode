#!/usr/bin/env python3
# vim: set ts=4 sw=4 noet:

diff = 0

with open("input") as f:
	for l in map(str.strip, f):
		diff -= len(l)
		diff += len(l.replace("\\", "\\\\").replace('"', '\\"')) + 2

print(diff)
