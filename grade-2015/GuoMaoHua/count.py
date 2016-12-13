#2016.12.10
import sys
import re
file_name = 'file.txt'
with open(file_name, 'r') as f:
    scentence = f.read()
    f.close()
majors = []
majors = scentence.split()
counts = []
print majors
for major in majors:
    counts.append(majors.count(major))
print counts
c = dict(zip(majors,counts))
print c
def fun(c):
    d = sorted(c.iteritems(),key=lambda t:t[1],reverse = False)
    return d
d = fun(c)
n = len(d)
while n > 0:
    print d[n-1]
    print '\n'
    n -= 1
