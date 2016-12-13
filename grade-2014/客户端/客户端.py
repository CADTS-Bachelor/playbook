import xmlrpclib
import datetime

proxy = xmlrpclib.ServerProxy("http://localhost:8001/")
a,b=map(int, raw_input("please enter two numbers:").split())
x=input("which operation do you want to do:    1:add    2:subtract    3:miltiply    4:divide  ")
if x==1:
    print proxy.add(a,b)
elif x==2:
    print proxy.subtract(a,b)
elif x==3:
    print proxy.multiply(a,b)
elif x==4:
    print proxy.divide(a,b)
multicall = xmlrpclib.MultiCall(proxy)
multicall.today()
multicall.add(a,b)
multicall.subtract(a,b)
multicall.multiply(a,b)
multicall.divide(a,b)
result = multicall()
