# Angkan Biswas
# 19.05.2020
# To write & read a text file 


fileName = '/home/dell/PythonCode/Text/Write_Read.txt'

'''To write in a new text file'''
fp = open(fileName, 'w')					# 'w': write mode

imgPath = '/home/dell/Downloads/frog.jpeg'
fp.write(imgPath + '\n')
fp.close()

'''To read from a text file'''
fp = open(fileName, 'r')					# 'r': read mode
text = fp.read()
fp.close()
print(text)

'''To write in a new text file by replacing the previous text file'''
fp = open(fileName, 'w')					# 'w': write mode					
imgPath = '/home/dell/Downloads/name.png'
fp.write(imgPath + '\n')
fp.close()

'''To write in an existing text file'''
fp = open(fileName, 'a')					# 'a': appned mode					
imgPath = '/home/dell/Downloads/football.png'
fp.write(imgPath + '\n')
fp.close()
