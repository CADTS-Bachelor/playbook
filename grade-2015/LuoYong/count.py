#coding=utf-8
#这个只按照了次数排序，没有按照字典排序，能力有限
#by luoyong
#2016.12.12

import collections
import os
import sys

file1=raw_input("Input file's name:")
with open(file1) as file1:
    str1=file1.read().split(' ')

print "\n各单词出现的次数：\n %s" % collections.Counter(str1)
print collections.Counter(str1)['was']
