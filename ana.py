from textblob import TextBlob
import re
import matplotlib.pyplot as plt
import time 
f=open("doc4.txt","r")
l=[]
for i in f.readlines():
	c=[i]
	l.append(c)
cnt=0

initimt=time.time()
for i in l:
	b=TextBlob(str(i))
	pos=0
	neg=0
	comp=0
	sent=0
	plt.ion()

	for j in b.sentences:
		sent+=j.sentiment.polarity
		if j.sentiment.polarity>=0:
			pos+=j.sentiment.polarity
		else:
			neg+=j.sentiment.polarity
	comp=comp+sent
	t=int(time.time()-initimt)
	print(i)
	print(sent)
	print("positive:",pos,"negative",neg,"compound",comp)
	cnt+=1
	plt.axis([0,100,-2,2])
	plt.xlabel('time')
	plt.ylabel('sentiment')
	plt.plot([t],[pos],'go',[t],[neg],'ro',[t],[comp],'bo')
	plt.show()
	plt.pause(1)
	if cnt>50:
		break





