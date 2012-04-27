#!/usr/bin/env python
from __future__ import print_function, division
import sys, json

def iterate(curr, rules):

	#first check to make sure rules are ok.
	for r in rules:
		if(len(r) != 1):
			raise KeyError("Keys must be of len 1.")

	#Some rules can't be overwritten
	rules['F'] = 'F'
	rules['+'] = '+'
	rules['-'] = '-'

	return ''.join([rules[x.upper()] for x in curr]).upper()

def main():
	try:
		with open(sys.argv[1]) as f:
			inp = json.load(f)
	except IndexError:
		print('This program requires an input JSON file.')

	try:
		rules = inp['rules']
		start = inp['start']
		if 'growth' in inp:
			growth = inp['growth']
		else:
			growth = .5
		iters = inp['iters']
	except Exception, e:
		raise e

	result = start
	for i in range(iters):
		result = iterate(result, rules)

	print(repr(result))

if __name__ == '__main__':
	main()