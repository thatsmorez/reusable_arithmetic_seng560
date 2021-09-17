import math

def add(a, b):
	if type(a) == str or type(b) == str or type(a) == bool or type(b) == bool:
		print("Invalid input parameters! Both parameters must be a numeric value (integar or float ).");
		return None;
	else:
		return a+b

def subtract(a, b):
	if type(a) == str or type(b) == str or type(a) == bool or type(b) == bool:
		print("Invalid input parameters! Both parameters must be a numeric value (integar or float).");	
		return None;
	else:
		return a-b

def multiply(a, b):
	if type(a) == str or type(b) == str or type(a) == bool or type(b) == bool:
		print("Invalid input parameters! Both parameters must be a numeric value (integar or float).");	
		return None;
	else:
		return a*b


def divide (a, b):
	if type(a) == str or type(b) == str or type(a) == bool or type(b) == bool:
		print("Invalid input parameters! Both parameters must be a numeric value (integar or float).");	
		return None;
	elif b == 0:
		print("You cannot divide by 0. Please enter a valid denominator.")
		return None;
	else:
		return a/b


def square_root(a):
	if type(a) == str or type(a) == bool:
		print("Invalid imput parameters! The parameter must be a numeric value (integar or float).");
		return None;
	elif a < 0:
		print("The square root of a negative number doesn't exist in the real domain.");
		return None;
	else:
		return math.sqrt(a);


def exponent(a, b):
	if type(a) == str or type(b) == str or type(a) == bool or type(b) == bool:
		print("Invalid input parameters! Both parameters must be a numeric value (integar or float).");	
		return None;
	else:
		return a**b


def convert2Octal(a):
	return oct(a)


def convert2Hex(a):
	return hex(a)


def convert2Integer(a):
	return int(a)
	

def convert2Binary(a):
	return bin(a);
