# Angkan Biswas
# 24.04.2020
# To make a file list of image files inside subdiretories of directory


import os

dirPath = '/home/dell/downloads/'

subDirList = os.listdir(dirPath)
n = len(subDirList)
print(subDirList, n)
 
for i in range(n):
	imgDirPath = dirPath + subDirList[i]	
	imgList = os.listdir(imgDirPath)
	
	m = len(imgList)
	for j in range(m):
		imgPath = imgDirPath + '/' + imgList[j]		
		print(j, imgPath)
