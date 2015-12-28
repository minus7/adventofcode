#!/usr/bin/env python3
# vim: set ts=4 sw=4 noet:

liters = 150

with open("input") as f:
	containers = [int(l) for l in f]

combinations = 0
bits = len(containers)
for i in range(2**bits):
	sum = 0
	for j in range(bits):
		if i & (1 << j):
			sum += containers[j]
	if sum == liters:
		combinations += 1

print(combinations)
