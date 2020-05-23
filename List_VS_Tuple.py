# Angkan Biswas
# 23.05.2020
# To understand difference between list & tuple

'''	List	'''
x = [1, 2, 3, 4, 5]; print(x)
x[1] = 10; print(x) 				# List is mutable, i.e., list elements cab be changed

'''	Tuple	'''
y = (1, 2, 3, 4, 5); print(y)
# y[1] = 10; print(y)				# Error! tuple elements can not be changed. Tuple is immutable
y = (1, 2, 3, 4, 10); print(y)

''' for...loop on list & tuple '''
for i in x:
	print(i)
for i in y:
	print(i)
