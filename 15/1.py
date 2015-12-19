#!/usr/bin/env python3
# vim: set ts=4 sw=4 noet:

import numpy as np

ingredients = []
with open("input") as f:
	for l in f:
		l = l.replace(",", "").split()
		l = [int(x) for x in l[2:9:2]]
		ingredients.append(l)

ingredients = np.array(ingredients)

def weights(n, max=100):
	if n == 1:
		yield (max,)  # must return this number to get to 100 total sum
		return
	for i in range(1, max+1-(n-1)):
		for more in weights(n-1, max=max-i):
			yield (i, *more)

score = 0
for w in weights(ingredients.shape[0]):
	w = np.matrix(w)
	scores = w * ingredients
	scores[scores < 0] = 0
	score = max(score, np.prod(scores))

print(score)
