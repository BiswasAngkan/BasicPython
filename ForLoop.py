# Angkan Biswas
# 24.04.2020
# How to use for..loop

'''...1st way....'''

for i in range(10):
	print(i)

for i in range(3):
	for j in range(5):
		print(i, j)

for i in range(3):
	for j in range(5):
		for k in range(4):		
			print(i, j, k)

'''...2nd way(increment)...'''

for i in range(2, 20):
	print(i)

for i in range(2, 20, 2):
	print(i)

'''...2nd way(decrement)...'''

for i in range(20, 2, -1):
	print(i)

for i in range(20, 2, -2):
	print(i)

'''...3rd way...'''

for i in [20, 2, 45, 7]:
	print(i)

for i in ['dog', 'cat', 'apple']:
	print(i)

'''...4th way...'''	

x = [i + 2 for i in [1, 2, 3, 4, 5]]
print(x)

x = [1, 2, 3, 4, 5]
y = [i + 2 for i in x]
print(y)
