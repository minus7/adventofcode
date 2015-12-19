#!/usr/bin/env python3
# vim: set ts=4 sw=4 noet:

operations = {}
def op(fn):
	operations[fn.__name__] = fn
	return fn

@op
def NOOP(a):
	return a

@op
def NOT(a):
	return (~a) % 0x10000

@op
def AND(a, b):
	return a & b

@op
def OR(a, b):
	return a | b

@op
def XOR(a, b):
	return a ^ b

@op
def LSHIFT(a, b):
	return (a << b) & 0xffff

@op
def RSHIFT(a, b):
	return a >> b


wires = {}
with open("input") as f:
	for l in f:
		inp, outp = l.strip().split(" -> ")
		parts = inp.split(" ")
		if len(parts) == 1:
			wires[outp] = (NOOP, inp)
		elif len(parts) == 2:
			op = operations[parts[0]]
			wires[outp] = (op, parts[1])
		elif len(parts) == 3:
			op = operations[parts[1]]
			wires[outp] = (op, parts[0], parts[2])

cache = {}
def evaluate_wire(wire):
	if wire in cache:
		return cache[wire]
	if wire.isnumeric():
		return int(wire)

	op, *args = wires[wire]
	args = [evaluate_wire(arg) for arg in args]
	cache[wire] = v = op(*args)
	return v
