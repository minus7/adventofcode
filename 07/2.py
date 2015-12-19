#!/usr/bin/env python3
# vim: set ts=4 sw=4 noet:

from common import evaluate_wire
import common

common.wires["b"] = (common.NOOP, str(evaluate_wire("a")))
common.cache = {}
print(evaluate_wire("a"))
