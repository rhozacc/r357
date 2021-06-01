# https://projecteuler.net/problem=5

# Smallest multiple

'''
2520 is the smallest number that can be divided by each of the 
numbers from 1 to 10 without any remainder.

What is the smallest positive number that is 
evenly divisible by all of the numbers from 1 to 20?
'''

from functools import reduce


def gcd(a, b):
	''' Returns greatest common divisor using Euclid's Algo '''
	while b:
		a, b = b, a%b
	return a


def lcm(a, b):
	''' Returns lowest common multiple '''
	return a * b // gcd(a, b)


def lcmm(*args):
	'''Returns lowest common multiple of args '''
	return reduce(lcm, args)


def lcm_seq(min, max):
	''' Return lcm of sequence '''
	seq = range(min, max+1)
	return reduce(lcm, seq)





print('Example:', lcm_seq(1, 10))
print('Soultion:',lcm_seq(1, 20))




