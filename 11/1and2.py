#!/usr/bin/env python3
# vim: set ts=4 sw=4 noet:

from itertools import groupby

data = [ord(x) - ord("a") for x in "cqjxjnds"]

bad_chr = tuple(ord(x) for x in "iol")

def print_pw(data):
	print("".join(chr(x + ord("a")) for x in data))

def pwiter():
	while True:
		for i in range(len(data)-1, -1, -1):
			data[i] = v = (data[i] + 1) % 26
			if v:
				# result not zero, thus no carry, we can stop
				break
		yield data

passwords = 0

for pw in pwiter():
	#print_pw(pw)
	# check "confusing" chars (i, o, l)
	for x in bad_chr:
		if x in data:
			continue
	#print("Check iol passed")

	# check for 2+ non-overlapping letter pairs
	if sum(1 for k, g in groupby(a for a, b in zip(pw[:-1], pw[1:]) if a == b)) < 2:
		continue
	#print("Check non-overlapping pairs passed")

	# check for 3-letter sequences (abc, cde, …)
	if not any(1 for a, b, c in zip(pw[:-2], pw[1:-1], pw[2:]) if a+1 == b and b+1 == c):
		continue
	#print("Check 3-letter sequence passed")

	print_pw(pw)
	passwords += 1
	if passwords >= 2:
		break
