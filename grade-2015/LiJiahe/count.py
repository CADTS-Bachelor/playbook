# coding=utf-8
#统计单词个数
#by 李佳贺
#2016.12.7
#输入英文纯文本文件，统计其中单词出现次数，输出首先按次数多少其次按字典顺序排列

import sys
if len(sys.argv)>1:
    file_name=sys.argv[1]
else:
    file_name=input('please input the filename:')
file=open(file_name,'r')
text=file.read()
file.close()
words=text.split()
counts=[]
while(words!=[]):
    word=words[0]
    counts.append([-1*words.count(word),word])
    for i in range(words.count(word)):
        words.remove(word)
counts.sort()
for j in range(len(counts)):
    print(counts[j][1],-1*counts[j][0])

