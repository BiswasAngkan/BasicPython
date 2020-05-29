# Angkan Biswas
# 29.05.2020
# To separate odd number & even number


evenNoList = []
oddNoList = []

while (True):
	x = int(input('Enter your number: ')) 
	
	if (x == -99999):
		break
	
	if (x % 2) == 0:
		evenNoList.append(x)		
		print('Even Number.')
	
	elif (x % 2) == 1:
		oddNoList.append(x)
		print('Odd Number.')
	
print('Even Number = {}'.format(evenNoList))
print('Odd Number = {}'.format(oddNoList))
