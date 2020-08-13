'''
This is a coding practice example.
Original work by CodingBat available at:
https://codingbat.com/prob/p173401
'''

# Warmup-1 > Sleep_in
'''
sleep_in(False, False) → True
sleep_in(True, False) → False
sleep_in(False, True) → True
'''

def sleep_in(weekday, vacation):
	if not weekday or vacation:
		return True
	else:
		return False

def sleep_in_short(weekday, vacation):
	return(not weekday or vacation)



# Warmup-1 > Monkey_trouble
'''
We have two monkeys, a and b, and the parameters a_smile and b_smile 
indicate if each is smiling. We are in trouble if they are both smiling 
or if neither of them is smiling. Return True if we are in trouble.

monkey_trouble(True, True) → True
monkey_trouble(False, False) → True
monkey_trouble(True, False) → False
'''

def monkey_trouble(a_smile, b_smile):
	if a_smile and b_smile:
		return True
	if not a_smile and not b_smile:
		return False

def monkey_trouble_short(a_smile, b_smile):
	return((a_smile and b_smile) or (not a_smile and b_smile))

def monkey_trouble_veryShort(a_smile, b_smile):
	return(a_smile == b_smile)



