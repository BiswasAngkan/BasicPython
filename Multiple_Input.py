# Angkan Biswas
# 22.05.2020
# To take multiple & put into lists


'''	Case-1	'''
nameList = []
for i in range(10):
	name = input('What is your name: ')		
	nameList.append(name)

print('Output = {}'.format(nameList))	

		
'''	Case-2	'''
evenNoList = []
oddNoList = []
for i in range(10):
	x = input('Enter your number: ') 
	x = int(x)
	
	if (x % 2) == 0:
		evenNoList.append(x)		
		print('Even Number.')
	
	elif (x % 2) == 1:
		oddNoList.append(x)
		print('Odd Number.')
	
print('Even Number = {}'.format(evenNoList))
print('Odd Number = {}'.format(oddNoList))
