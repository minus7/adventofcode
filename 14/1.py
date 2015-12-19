#!/usr/bin/env python3
# vim: set ts=4 sw=4 noet:

from collections import namedtuple

Stats = namedtuple("Stats", ("speed", "duration", "rest"))

reindeer = {}
with open("input") as f:
	for l in map(str.split, f):
		reindeer[l[0]] = Stats(int(l[3]), int(l[6]), int(l[-2]))

total_duration = 2503
results = []
for r in reindeer.values():
	time = 0
	distance = 0
	while time + r.duration <= total_duration:
		time += r.duration + r.rest
		distance += r.speed * r.duration
	if time < total_duration:
		distance += r.speed * (total_duration - time)
	results.append(distance)

print(max(results))
