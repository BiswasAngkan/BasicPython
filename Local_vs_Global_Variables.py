# Angkan Biswas
# 26.5.2020
# To understand the difference between local and global variables.

def main():
	f1()
	f3()
	f5()
	f4()
	f6()
	f4()

def f6():
	global b

	''' 'b' is a global variable. '''
	print('Inside f6(): Global b = {}'.format(b))	

	''' 'b' is a global variable now. Changing its value will affect 
		 all other functions, since it can be seen by  all other functions. 
	'''
	b = 5000
	print('Inside f6(): Global b = {}'.format(b))

def f5():
	''' 'b' is a global variable. '''
	print('Inside f5(): Global b = {}'.format(b))	

def f3():
	global b

	b = 10
	print('Inside f3(): b = {}'.format(b))

	''' 'a' is a global variable. It does not need to be sent to any functions 
		as arguments, since all functions can see it.
	'''
	f4()

	''' 'b' is a global variable. Changing its value will affect 
		all other functions, since it can be seen by all other functions.'''
	b = 30		
	print('Inside f3(): b = {}'.format(b))

	f4()

def f4():
	print('Inside f3(): b = {}'.format(b))	

def f1():
	a = 10
	print('Inside f1(): a = {}'.format(a))

	''' 'a' is a local variable of f1(). One of its copy can be sent 
		to another function as argument. If any changes happens inside that
		function, that will not affect it.	'''
	f2(a)

	''' 'a' is a local variable of f1(). Changing its value will not affect 
		other functions, since it cannot be seen by other functions.'''
	a = 30		
	print('Inside f1(): a = {}'.format(a))	


def f2(a):
	'''	'a' is a local variable of f2(). Initially it is holding the value sent
		by the functions which call f1().
	'''
	print('Inside f2(): a = {}'.format(a))

	''' 'a' is a local variable of f2(). Changing its value will not affect 
		other functions, since it cannot be seen by other functions.'''
	a = 40
	print('Inside f2(): a = {}'.format(a))

main()
