#!/usr/bin/env python3
# vim: set ts=4 sw=4 noet:

import operator

sues = {}
with open("input") as f:
	for l in map(str.strip, f):
		sue, properties = l.split(": ", 1)
		sue_id = int(sue.split(" ")[1])
		properties = properties.split(", ")
		properties = map(lambda x: x.split(": "), properties)
		properties = map(lambda x: (x[0], int(x[1])), properties)
		properties = dict(properties)
		sues[sue_id] = properties

reference = {
	"children": 3,
	"cats": 7,
	"samoyeds": 2,
	"pomeranians": 3,
	"akitas": 0,
	"vizslas": 0,
	"goldfish": 5,
	"trees": 3,
	"cars": 2,
	"perfumes": 1,
}


for sue, properties in sues.items():
	for prop_name, prop in properties.items():
		op = operator.eq
		if prop_name in ("cats", "trees"):
			op = operator.gt
		if prop_name in ("pomeranians", "goldfish"):
			op = operator.lt
		if not op(prop, reference[prop_name]):
			break
	else:
		print(sue)
