import numpy as np
import pandas as pd
import cv2
import imghdr
#reading the reference CSV
index=["color","color_name","hex","R","G","B"]
csv = pd.read_csv('colors.csv', names=index, header=None)

def getColorName(img,x,y):
	print(x)
	print(y)
	x=500
	y=100
	img = cv2.imread("dog.jpg")
	b, g, r = img[y, x]
	print(imghdr.what("dog.jpg"))
	cv2.imshow('dog',img)
	B = int(b)
	G = int(g)
	R = int(r)
	minimum = 10000
	for i in range(len(csv)):
		d = abs(R - int(csv.loc[i, "R"])) + abs(G - int(csv.loc[i, "G"])) + abs(B - int(csv.loc[i, "B"]))
		if(d <= minimum):
			minimum = d
			cname = csv.loc[i, "color_name"]
	if cv2.waitKey(1) == ord('q'):
		cv2.destroyAllWindows()
	return cname

