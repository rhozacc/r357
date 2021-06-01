# https://projecteuler.net/problem=3

# Laregest prime factor

'''
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
'''



def Problem(n):
	i = 2
	while i*i <=n:
		if n%i:
			i += 1
		else:
			n//=i  # n = floor division of n//i
	
	return n							



print('Example:', Problem(10))
print('Soultion:',Problem(600851475143))




