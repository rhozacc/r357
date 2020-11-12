# https://projecteuler.net/problem=6

# Sum square difference

'''
The sum of the squares of the first ten natural numbers is,
1**2 + 2**2 + ... + 10**2 = 385

The square of the sum of the first ten natural numbers is,
(1+2+...+10)**2 = 55**2 = 3025

Hence the difference between the sum of the squares of the 
first ten natural numbers and the square of the sum is .
3025 - 385 = 2640

Find the difference between the sum of the squares of the 
first one hundred natural numbers and the square of the sum.
'''


def Problem(n):
	''' Return the difference between 
		the sum of squares of the first n natural numbers and
		the square of the sum
	'''

	a, b = [], []
	
	for n in range(1, n+1):
		a.append(n**2)
		b.append(n)
	
	return((sum(b)**2)-sum(a))



print('Example:', Problem(10))
print('Soultion:',Problem(100))




