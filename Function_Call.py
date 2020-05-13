# Angkan Biswas
# 13.05.2020
# To define & call functions 

def f1():						# Define f1 [f1 = My function]
	a = 5						# a = Variable 
	print(a) 					# Call print [print = Python's function], a = Variable/Argument/Parameter
	f2()						# Call f2 [f2 = My function]

def f2():						# Define f2 [f2 = My function]
	a = 4 						# a = Variable
	print(a) 					# Call print [print = Python's function], a = Variable/Argument/Parameter
	f3(a) 						# Call f3 [f3 = My function], a = Variable
	b = f4(a) 					# a = Variable/Argument/Parameter, b = Variable, Call f4 [f4 = My function]
	print(b) 					# Call print [print = Python's function], b = Variable/Argument/Parameter

def f3(b):						# Define f3 [f3 = My function], b = Variable
	a = 3						# a = Variable
	print(a) 					# Call print [print = Python's function], a = Variable/Argument/Parameter
	a = a + b					# a, b = Variables
	print(a) 					# Call print [print = Python's function], a = Variable/Argument/Parameter
		

def f4(c):						# Define f4 [f4 = My function], c = Variable
	a = 2						# a = Variable
	print(a) 					# Call print [print = Python's function], a = Variable/Argument/Parameter	
	b = a + c 					# a, b, c = Variables
	print(b)					# Call print [print = Python's function], b = Variable/Argument/Parameter 
	
	return a					# a = Variable/Argument/Parameter

f1()							# Call f1 [f1 = My function]
