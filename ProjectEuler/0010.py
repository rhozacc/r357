#!/usr/local/bin/python3

'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

from math import sqrt


sieve = list(range(2000000+1))
sieve[1] = 0

for n in range(2, int(sqrt(2000000))+1):
    if sieve[n] > 0:
        for i in range(n*n, 2000000+1, n):
            sieve[i]=0

print(sum(sieve))


