#list append
fruits = ['apple', 'banana', 'cherry']
fruits.append("orange")
print(fruits)

# list clear

fruits = ['apple', 'banana', 'cherry', 'orange']

fruits.clear()

print(fruits)



a=[10,20,30,40,50,80]
s=a[0]
second=0
for i in a:
    if i < s:
        second=s

        s=i

    print(second)