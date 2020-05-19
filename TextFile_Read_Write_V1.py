# Angkan Biswas
# 19.05.2020
# To write & read a text file 


fileName = '/home/dell/PythonCode/Text/Write_Read.txt'

'''To write in a text file'''
fp = open(fileName, 'w')

imgPath = '/home/dell/Downloads/frog.jpeg'
fp.write(imgPath)
fp.close()

'''To read from a text file'''
fp = open(fileName, 'r')
text = fp.read()
fp.close()
print(text)
