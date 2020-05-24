# Angkan Biswas
# 24.05.2020
# To decide whether a number is even or odd.
# Even number: remainder will be 0 when it is divided by 2. Example (2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 42 44 46 48 50 )
# Odd number : remainder will be 0 when it is divided by 3. Example (1 3 5 7 9 11 13 15 17 19 21 23 25 27 29 31 33 35 37 39 41 43 45 47 49)
# Float number : remainder will not be 0 when it is divided by 2 & 3

x = input('Enter your number: ') 

if (float(x) % 2) == 0:
	print('Even Number.')
else:
	if (float(x) % 3) == 0:
		print('Odd Number.')
	else:
		print('Float Number.')
