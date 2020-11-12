# https://projecteuler.net/problem=4

# Largest palindrome product

'''
A palindromic number reads the same both ways.

The largest palindrome made from the product of 
two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of 
two 3-digit numbers.
'''

# get all products - backwards?
	# chekck for palindromes


def Palindrome(x):
	'''Returns True if Palindrome'''
	lst = [int(n) for n in str(x)]
	if lst == lst[::-1]: 
		return True



def LaregstPalindromeProduct(n):
	a = []
	for i in range(10**n, 1, -1):
		for j in range(i, 1, -1):
			x = i*j
			if Palindrome(x): a.append(x)
	return max(a)



print('Example:', LaregstPalindromeProduct(2))
print('Soultion:',LaregstPalindromeProduct(3))




