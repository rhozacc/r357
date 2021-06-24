#!/usr/local/bin/python3
# https://projecteuler.net/problem=9
# 

'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''


for b in range(1, 1000):
    for a in range(1,b):
        c2 = a**2 + b**2
        if c2 == (1000-a-b)**2:
            print(a*b*(1000-a-b))
        else:
            continue



