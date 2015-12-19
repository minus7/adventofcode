#!/usr/bin/env python3
# vim: set ts=4 sw=4 noet:

from itertools import groupby

data = map(int, "3113322113")

for _ in range(40):
	new_data = []
	for k, g in groupby(data):
		new_data.append(len(tuple(g)))
		new_data.append(k)
	data = new_data

print(len(data))
