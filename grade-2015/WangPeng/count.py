#author bird
#date 2016-12-10
#统计英文单词出现频率并按照热度和字典顺序输出


import re
import sys
def printlist(list):
    for value,key in list :
        print str(key) + " : " + str(value)
with open(sys.argv[1],'r') as file :
    data = file.read()
    words = re.compile('[a-zA-Z0-9]+')
    dict = {}
    for x in words.findall(data) :
        if x not in dict :
            dict[x] = 1
        else :
            dict[x] += 1
    list1 = dict.items()
    list2 = []
    for key,value in list1 :
        list2.append((value,key))
    list2.sort(reverse = True)
    temp = list2[0][0]
    sum = 0
    flag = 0
    sum2 = sum
    length = len(list2)
    i = 0
    while i < length :
        if temp == list2[i][0]:
            sum += 1
        else:
            flag = 1
            temp = list2[i][0]
            i -= 1
        if flag == 1:
            if sum2 == 0:
                printlist(list2[sum2 + sum - 1: : -1])
            else:
                printlist(list2[sum2 + sum - 1: sum2 - 1 : -1])
            sum2 += sum
            sum = 0
            flag = 0
        i += 1
    printlist(list2[sum2 + sum - 1: sum2 - 1 : -1])

