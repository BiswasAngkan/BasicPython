# Angkan Biswas
# 24.05.2020
# To understand how to use dictionay

'''	1st Dictionary	'''
x = {'A': 'angkan', 'B': 'biswas', 'C': 'cat'}			# Dictionary x contains single values
print(x['A'], x['B'], x['C'])

'''	2nd Dictionary	'''
a = ['Angkan', 'Akheen', 'Adalat', 'Arunachal']
b = ['Bibrity', 'Bat', 'Ball', 'Bari', 'Bihar']
c = ['Cat', 'Cool', 'Crow', 'Cow', 'Cook']
d = ['Dhanmondi', 'Dog', 'Door', 'Duck', 'Dhaka']
e = ['Elephent', 'Egale', 'East', 'Easy', 'Eat']

y = {'A': a, 'B': b, 'C': c, 'D': d, 'E': e}			# Dictionary y contains lists
print(y['C'])
print(y['B'][2])

'''	3rd Dictionary	'''
t = (1, 2, 3, 4, 5)
z = {'A': x, 'B': b, 'C': 12.3, 'D': 'Nam', 'E': e, 'No': t}	# Dictionary z contains single values, list, tuple & dictionary 
print(z['B'][3], z['C'])
