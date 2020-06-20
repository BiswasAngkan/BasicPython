# Angkan Biswas
# Numpy Array Initialization
# 20.06.2020

import numpy as np

'''	A numpy array having 10 elements where all elements 
	are initialized to float value, 0.	'''
a = np.zeros((10,))
print('a: {}'.format(a))

'''	A numpy array having 10 elements where all elements
	are initialized to integer value, 0.	'''
b = np.zeros((10,), dtype = np.uint8)
print('b: {}'.format(b))

'''	A numpy array having 10 elements where all elements
	are initialized to integer value, 1.	'''
c = np.ones((10,), dtype = np.uint8)
print('c: {}'.format(c))

'''	A numpy array having 10 elements where all elements
	are initialized to integer value, 100.	'''
d = [100] * 5
print('d: {}'.format(d))

'''	A numpy array having 10 elements where all elements
	are initialized to string, 'Angkan'.	'''
e = ['Angkan'] * 10
print('e: {}'.format(e))
