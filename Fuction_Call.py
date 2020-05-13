# Angkan Biswas
# 13.05.2020
# To define & call functions 

def f1():
	a = 5
	print(a)
	f2()

def f2():
	a = 4
	print(a)
	f3(a)
	b = f4(a)
	print(b)

def f3(b):
	a = 3
	print(a)
	a = a + b
	print(a)
		

def f4(c):
	a = 2
	print(a)	
	b = a + c
	print(b)  
	
	return a

f1()
