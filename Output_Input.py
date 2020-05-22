# Angkan Biswas
# 22.05.2020
# To use input output function

'''Output'''
print('I am Angkan Biswas')
x = 'Angkan Biswas'
print('{}'.format(x))
print('Hello!!! {}. How are you?'.format(x))

x = 10
y = 20
print('{} + {}'.format(x,y))
print('{} + {} = {}'.format(x, y, x + y))

'''Input'''
x = input()					# Bad way
print(x)					# Bad way

print('x = {}'.format(x))			# Good way
y = input('What is your name: ')		# Good way
print('y = {}'.format(y))			# Good way
