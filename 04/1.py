#!/usr/bin/env python3
# vim: set ts=4 sw=4 noet:

from hashlib import md5
from itertools import count

data = b"yzbqklnj"

for i in count(1):
	digest = md5(data + str(i).encode()).hexdigest()
	if digest.startswith(5*"0"):
		print(i)
		break
