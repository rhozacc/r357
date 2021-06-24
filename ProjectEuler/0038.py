#!/usr/local/bin/python3
#Problem 38

'''
Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?
'''


def ConcatenatedProduct(base, multiplier_list):
    concat = [multiple*base for multiple in multiplier_list]
    return(int(''.join(map(str,concat))))


def isPandigit(digit):
    _check = list(str(digit))
    check = [int(i) for i in _check]
    pan = [1,2,3,4,5,6,7,8,9]
    if set(check) == set(pan):
        return True
    else:
        return False


# init for 1,2 and put them on list
multiplier_list = [1,2]
pandigits = []


''' Using pure logic:
1. Base must be <5 digits since n has to be >1.
2. We are given a candidate that starts with 9!!!
    so the base needs to start w 9!
3. If base is len2, we're not generating a len9 number
    as n=3 generates len8 and n=4 generates len11
4. If base is len3, n=3 is len7, n=4 is len11.

5. ---> Leaves us with len4 base and start w 9.
'''


result = 0
for i in range(9876, 9123, -1):
    result = ConcatenatedProduct(i, multiplier_list)
    if isPandigit(result):
        print(result)
        break
        





