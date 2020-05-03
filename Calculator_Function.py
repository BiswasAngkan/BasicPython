# Angkan Biswas
# 03.05.2020
# To use user defined function

def subtraction(a, b):
	c = a - b
	print('{} - {}: {}'.format(a, b, c))

def addition(a, b):
	c = a + b
	print('{} + {}: {}'.format(a, b, c))

def multiplication(a, b):
	c = a * b
	print('{} * {} = {}'.format(a, b,c))

def division(a, b):
	c = a / b
	print('{} / {} = {}'.format(a, b, c))

def calculator():
	x = int(input('Enter a number: '))
	y = int(input('Enter another number: '))

	subtraction(x, y)
	addition(x, y)
	multiplication(x, y)
	division(x, y)
	
calculator()
