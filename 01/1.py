#!/usr/bin/env python3
# vim: set ts=4 sw=4 noet:

from collections import Counter

with open("input") as f:
	data = f.read()

cnt = Counter(data)

print(cnt["("] - cnt[")"])
