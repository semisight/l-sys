#!/usr/bin/env python
from __future__ import print_function, division
import sys, json

def __check_rule(r):
	if len(r) != 1:
		sys.stdout.write('WARNING! All multicharacter rules will be ignored.\n')
	elif r == 'F':
		sys.stdout.write('WARNING! \'F\' may not be used as a rule.\n')
	elif r == '+':
		sys.stdout.write('WARNING! \'+\' may not be used as a rule.\n')
	elif r == '-':
		sys.stdout.write('WARNING! \'-\' may not be used as a rule.\n')

def __single_pass(curr, rules):
	return ''.join([rules[x.upper()] for x in curr]).upper()

def iterate(path, **kwargs):
	with open(path) as f:
		inp = json.load(f)

	rules = start = iters = growth = size = None

	#keyword args take precedence over json specs
	if rules in kwargs:
		rules = kwargs['rules']

	if start in kwargs:
		start = kwargs['start']

	if iters in kwargs:
		iters = kwargs['iters']

	if growth in kwargs:
		growth = kwargs['growth']

	if size in kwargs:
		size = kwargs['size']

	try:
		if rules == None:
			rules = inp['rules']

		if start == None:
			start = inp['start']

		if iters == None:
			iters = inp['iters']

		if growth == None:
			if 'growth' in inp:
				growth = inp['growth']
			else:
				growth = .5

		if size == None:
			if 'size' in inp:
				size = inp['size']
			else:
				size = 512
	except IndexError, e:
		sys.stdout.write('You need to specify all of the parameters!\n')
		raise e

	#first check to make sure rules are ok.
	for r in rules:
		__check_rule(r)

	#Some rules can't be overwritten
	rules['F'] = 'F'
	rules['+'] = '+'
	rules['-'] = '-'

	result = start
	for i in range(iters):
		result = __single_pass(result, rules)

	return result, iters, growth, size

def main():

	result = start
	for i in range(iters):
		result = iterate(result, rules)

	print(repr(result))

if __name__ == '__main__':
	main()