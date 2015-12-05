#!/usr/bin/env python3
# vim: set ts=4 sw=4 noet:

with open("input") as f:
	data = f.read()

pos = 0
for i, c in enumerate(data, 1):
	pos += 1 if c == "(" else -1
	if pos == -1:
		print(i)
		break
