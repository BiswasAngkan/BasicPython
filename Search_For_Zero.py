# Angkan Biswas
# 29.05.2020
# To read integers from the keyboard & display only zeros 


intList = []
n = 10

for i in range(n):
	print('{}/{}'.format(i+1, n))
	x = int(input('Enter a no:'))
	
	if((x == -9999) or (x == 21)):
		break

	if(x == 0):
		intList.append(x)

print('Entered Integer: {}'.format(intList))	
	
