'''
Write a Python function, fourthPower, that takes in one number and returns that value raised to the fourth power.

You should use the square procedure that you defined in an earlier exercise (you don't need to redefine square in this box; when you call square, the grader will use our definition).

This function takes in one number and returns one number.
'''

import w2_simple_programs_ex2_square

def fourthPower(x):
	'''
	x: int or float.
	'''
	square = w2_simple_programs_ex2_square.square # Only here so we can import square - auto tester already has this imported
	return square(square(x))
	
	
print("2^4 = " + str(fourthPower(2)))