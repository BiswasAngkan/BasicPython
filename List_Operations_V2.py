# Angkan Biswas
# 22.05.2020
# To perform for...loop in one line

x = range(10)
print(x)
y = list(range(10))
print(y)
y = [a+2 for a in x]
print(y)
y = [a*3 for a in x]
print(y)
y = [a*2 for a in [a+2 for a in x]]
print(y)
