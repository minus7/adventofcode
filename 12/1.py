#!/usr/bin/env python3
# vim: set ts=4 sw=4 noet:

from json import load

sum = 0
def parse_int(v):
	global sum
	v = int(v)
	sum += v
	return v

with open("input") as f:
	doc = load(f, parse_int=parse_int)

print(sum)
