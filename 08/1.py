#!/usr/bin/env python3
# vim: set ts=4 sw=4 noet:

diff = 0

with open("input", "rb") as f:
	for l in map(bytes.strip, f):
		diff += len(l.decode("ascii"))
		diff -= len(l[1:-1].decode("unicode_escape"))

print(diff)
