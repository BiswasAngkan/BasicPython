# Angkan Biswas
# To rotate elements of a list.
# 02.07.2020

a = [1, 2, 3, 4, 5, 6]

n = len(a)

'''	To rotate a list 1 step left.	'''
i = 1
b = a[i:] + a[:i] 

print('a: {}'.format(a))
print('b: {}\n'.format(b))
	
'''	To rotate a list 2 steps left.	'''
i = 2
b = a[i:] + a[:i] 

print('a: {}'.format(a))
print('b: {}\n'.format(b))

'''	To rotate a list 2 steps right.	'''
i = 2
b =  a[-i:] + a[:-i] 

print('a: {}'.format(a))
print('b: {}\n'.format(b))

'''	To rotate a list multiple times.	'''
for i in range(n):
	b = a[i:] + a[:i]  
	print('b: {}'.format(b))
