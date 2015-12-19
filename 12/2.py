#!/usr/bin/env python3
# vim: set ts=4 sw=4 noet:

from json import load

def process(o):
	sum = 0
	if isinstance(o, dict):
		o = list(o.values())
		if "red" in o:
			return 0
	for item in o:
		if isinstance(item, int):
			sum += item
		elif isinstance(item, (list, dict)):
			sum += process(item)
	return sum

with open("input") as f:
	doc = load(f)

print(process(doc))
