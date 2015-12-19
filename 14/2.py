#!/usr/bin/env python3
# vim: set ts=4 sw=4 noet:

from collections import defaultdict

class Stats:
	def __init__(self, speed, duration, rest):
		self.speed = speed
		self.duration = duration
		self.rest = rest
		self.distance = 0
		self.running = True
		self.counter = duration
	
	def tick(self):
		self.counter -= 1
		if self.running:
			self.distance += self.speed
		if self.counter == 0:
			self.running = not self.running
			self.counter = self.rest if not self.running else self.duration


reindeer = {}
with open("input") as f:
	for l in map(str.split, f):
		reindeer[l[0]] = Stats(int(l[3]), int(l[6]), int(l[-2]))

total_duration = 2503
results = defaultdict(int)
for i in range(total_duration):
	max_distance = 0
	for r in reindeer.values():
		r.tick()
		max_distance = max(max_distance, r.distance)
	for name, r in reindeer.items():
		if r.distance == max_distance:
			results[name] += 1

print(max(results.values()))
