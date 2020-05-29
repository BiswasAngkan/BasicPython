# Angkan Biswas
# 28.05.2020
# To read strings from the keyboard and find a specific character in those strings.

strList = []
n = 100

for i in range(n):
	'''	Read string	'''
	print('{}/{}'.format(i+1, n))
	x = input('Enter a string: ')
	
	'''	Check whether it is the break statement.	'''
	if ((x == 'Exit') or (x == 'exit')):
		break
	
	'''	Find 'a' in the string.	'''
	m = len(x)
	found = False
	for j in range(m):
		if (x[j] == 'a'):
			found = True
			break	# Stop searching if we find 'a'.

	'''	Insert the string into a list if it has 'a'.	'''
	if (found == True):
		strList.append(x)
	
print('Entered Strings: {}'.format(strList))


