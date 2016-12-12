#统计单词个数
#by 李佳贺
#2016.12.7
#输入英文纯文本文件，统计其中单词出现次数，输出首先按次数多少其次按字典顺序排列

import sys
import re
if len(sys.argv)>1:
    file_name=sys.argv[1]
else:
    file_name=input('please input the filename:')
file=open(file_name,'r')
text=file.read()
file.close()
words={}
for word in re.findall(r'[a-zA-Z0-9]+',text):
    words[word]=words.get(word,0)+1
counts=sorted(words.items(),key=lambda x:(-x[1],x[0]))
for j in range(len(counts)):
    print(counts[j][0],counts[j][1])
