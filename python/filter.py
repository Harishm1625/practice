a=[1,2,3,4,5,6,7,8,9,10]

def fil(a):
    return a % 2== 0
even=filter(fil,a)

print(list(even))

#using lambada function

a=[1,2,3,4,5,6,7,8,9,10,12,14,16,18,20]

result=filter(lambda x:x % 2==0, a)

print(list(result))

words = ['apple', 'an', 'banana', 'cat', 'dog']

# Lambda function la length > 3 nu check pannrom
long_words = filter(lambda word: len(word) >=3, words)

print(list(long_words))













