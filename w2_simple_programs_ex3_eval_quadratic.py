'''
Write a Python function, evalQuadratic(a, b, c, x), that returns the value of the quadratic 
a ⋅ x^2 + b ⋅ x + c

This function takes in four numbers and returns a single number.
'''

def evalQuadratic(a, b, c, x):
	'''
	a, b, c: numerical values for the coefficients of a quadratic equation
	x: numerical value at which to evaluate the quadratic.
	'''
	
	left_side = a * (x**2)
	right_side = (b * x) + c
	
	return left_side + right_side
	
print("Evaluating quadrilatric abcx with values -0.92, 2.83, 5.71, -3.13: " + str(evalQuadratic(-0.92, 2.83, 5.71, -3.13)))