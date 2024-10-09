#
a=[1,2,3,4,5,6]

def hoc(a):
    return a*2

result=map(hoc,a)
print(set(result))

# b=hoc(a)# jist call a function only not using map
# print(b)

#


s=[2,4,6,8]
v=[1,2,3,4]

k=map(lambda x,y:x+y,s,v)
print(list(k))

l=map(lambda a,b:a*b,s,v)
print(list(l))