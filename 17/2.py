#!/usr/bin/env python3
# vim: set ts=4 sw=4 noet:

liters = 150

with open("input") as f:
	containers = [int(l) for l in f]

bits = len(containers)
combinations = 0
num_containers = bits
for i in range(2**bits):
	sum = 0
	num = 0
	for j in range(bits):
		if i & (1 << j):
			num += 1
			sum += containers[j]
	if sum == liters and num <= num_containers:
		if num < num_containers:
			num_containers = num
			combinations = 0
		combinations += 1

print(combinations)
