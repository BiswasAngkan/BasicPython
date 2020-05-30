# Angkan Biswas
# 30.05.2020
# Write a program to read a sequance of numbers at first from the keyboard and then find a specific number into that sequence.


'''	Read numbers and put them into a list until -9999 is typed. '''
numList = []

while(True):
	x = int(input('Enter a no: '))
	
	if(x == -9999):
		break
	numList.append(x)
print(numList)
	
'''	Read the specific number which need to be searched and put it into the searhKey.	'''
searchKey = int(input('Search No.: '))

'''	Estimate the length of the list of numbers.	'''
n = len(numList)

'''	Search the specific number into the list of numbers using searchKey and the length of the list. (for....loop can be used)	'''
for i in range(n):
	if(numList[i] == searchKey):
		print('{} is found'.format(searchKey))	
