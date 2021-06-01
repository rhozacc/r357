# https://projecteuler.net/problem=1

# Multiples of 3 and 5

'''
If we list all the natural numbers below 10 that are 
multiples of 3 or 5, we get 3, 5, 6 and 9. 
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000. 
'''


def Problem1(n):
	a = []
	# append only if mod 3 or mod 5
	for n in range(1, n):
		if n%3==0 or n%5==0:
			a.append(n)

	# Return sum
	return sum(a)



print('Example:', Problem1(10))
print('Soultion:',Problem1(1000))




