# https://projecteuler.net/problem=7

# 10001st prime

'''
By listing the first six prime numbers:
2,3,5,7,11,13

we can see that:
6th prime is 13.

What is the 10001st prime number?
'''
# Generate primes while len(primes)<=10001 then print(primes[-1])

### Sieve of Eratosthenes
# Starts at 2 and crosses all n%2==0 (even numbers).
# Continues to 3 and crosses all n%3==0
# 4 is out, next is 5. Then 7, 11, 13.
# All divisors are primes.


def gen_primes():	
	D = {}
	q = 2
	
	while True:
		if q not in D:
			# q is a new prime
			# Yield it and mark its first multiple that isn't already marked in prev iters
			yield q
			D[q*q] = [q]

		else:
			# q is composite.
			# D[q] is the list of primes that divide it.
			for p in D[q]:
				D.setdefault(p+q, []).append(p)
			del D[q]
	
		q+=1


def Problem(n):
	primes = [p for i, p in zip(range(n), gen_primes())]
	return(primes[-1])


print('Example:', Problem(6))
print('Soultion:',Problem(10001))




