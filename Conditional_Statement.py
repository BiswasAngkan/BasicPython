# Angkan Biswas
# 23.05.2020
# To use if_else statement

'''1st case'''
x = input('Insert a Number: ')
x = int(x)
if x < 5:
	print('Welcome')

if x < 5:
	print('Welcome')
else:
	print('Please Go Back!!!')

'''2nd case'''
for i in range(20):
	if i < 5: 
		print(0)
	else:
		print(5)

'''3rd case'''
x = range(20)
y = [0 if a < 5 else 5 for a in x]
print(y)
