# Angkan Biswas
# 29.05.2020
# To read integers from the keyboard & display only a specefic number 


numList = []
n = 10
searchKey = int(input('Search No.: '))

for i in range(n):
	print('{}/{}'.format(i+1, n))
	x = int(input('Enter a no: '))
	
	if(x == -9999):
		break

	if(x == searchKey):
		numList.append(x)

print('Entered Integer: {}'.format(numList))	
	
