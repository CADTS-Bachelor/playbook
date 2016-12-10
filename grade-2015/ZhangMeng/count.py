#zm
#2016.12.09
#
import re
import sys
title=raw_input("Input file's name:")
last=".txt"
title=title+last
f=open(title)
Sentence=f.read()
f.close()
words_dic={}
for i in re.findall(r'[a-zA-Z0-9]+',Sentence):
	if i in words_dic:
		words_dic[i]+=1
	else:
		words_dic[i]=1
words_list=sorted(words_dic.iteritems(),key=lambda d:(d[1],d[0]),reverse=True)
k=j=0
while k<len(words_list):
	temp=words_list[j][1]
	if words_list[k][1]==temp:
		k+=1
	else:
		t=k
		while j<k:
			print words_list[k-1][0]+':',words_list[k-1][1]
			k-=1
		j=k=t
while j<k:
	print words_list[k-1][0]+':',words_list[k-1][1]
	k-=1
raw_input("Press <enter>")