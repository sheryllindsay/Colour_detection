import numpy as np
import pandas as pd

#reading the reference CSV
index=["color","color_name","hex","R","G","B"]
csv = pd.read_csv('colors.csv', names=index, header=None)

def most_frequent(List): 
	return max(set(List), key = List.count) 

def getColorName(img,x,y):
	margin=20
	xa=[]
	ya=[]
	colors=[]
	xa.append(int(x+margin))
	xa.append(int(x-margin))
	xa.append(int(x+margin))
	xa.append(int(x-margin))
	ya.append(int(y-margin))
	ya.append(int(y-margin))
	ya.append(int(y+margin))
	ya.append(int(y+margin))
	for i in range(0, len(xa)):
		xt = xa[i]
		yt = ya[i]
		if(xt<0):
			xt=0
		if(yt<0):
			yt=0
		b,g,r = img[yt,xt]
		B = int(b)
		G = int(g)
		R = int(r)
	       
		minimum = 10000
		for i in range(len(csv)):
			d = abs(R- int(csv.loc[i,"R"])) + abs(G- int(csv.loc[i,"G"]))+ abs(B- int(csv.loc[i,"B"]))
			if(d<=minimum):
				minimum = d
				ct = csv.loc[i,"color_name"]
		colors.append(str(ct))	 
	cname=most_frequent(colors) 
	print(colors)
	return cname

