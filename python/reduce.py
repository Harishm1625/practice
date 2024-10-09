
from functools import reduce

a=[1,2,3,4,5,6,7,8,9,10]

def red(a,b):
    return a*b

result=reduce(red , a)

print(result)



d=["1","2","3","4","5"]

def add(x):
    return int(x) + int(x)

result= map(add , d)

print(list(result))



