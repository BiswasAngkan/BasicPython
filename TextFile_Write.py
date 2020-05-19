# Angkan Biswas
# 19.05.2020
# To write on a text file 

fileName = '/home/dell/PythonCode/Text/MallData.txt'

fp = open(fileName, 'w')
for i in range(1, 2001):
	filePath = '/home/dell/mall_dataset/frames/seq_00' + str(i).zfill(4) + '.jpg'
	print(filePath)
	fp.write(filePath + '\n')


fp.close()

