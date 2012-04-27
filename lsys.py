#!/usr/bin/env python
from __future__ import print_function, division
import json

def iterate(curr, rules):

	#first check to make sure rules are ok.
	for r in rules:
		if(len(r) != 1):
			raise KeyError("Keys must be of len 1.")

	return ''.join([rules[x] for x in curr])

if __name__ == '__main__':
	r = {"A": "AB", "B": "A"}
	print(repr(iterate('ABAABB', r)))