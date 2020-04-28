# Angkan Biswas
# 28.04.2020
# How to use if condition


import os
import cv2

imgPath = '/home/dell/downloads/rickshaw/1.maxresdefault.jpg' 

imgStatus = os.path.isfile(imgPath)				# check whether image file exists or not
print(imgStatus)

if imgStatus == True:						# if file exists then execute line 15 to 21
	img = cv2.imread(imgPath)
	h, w, ch = img.shape
	if h > 512:
		imgResize = cv2.resize(img, (512, 512))

	cv2.imshow('Rickshaw', imgResize)
	cv2.waitKey(0)
