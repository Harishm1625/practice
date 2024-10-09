#functions
#
# # function decleration
# #def function name
#
# def empid():
#     print("this is for declaring function")
# empid()#-- function call panaradhu
#
# # function without argument
#
# def add():
#     a=5
#     b=5
#     c=a+b
#     print(c)
# add()
#
# # function with argument
# #why we using argument means = vera vera values use panarathukaga like
#
# def sub(a,b):
#     c=a-b
#     print(c)
# sub(5,2)
# sub(15,2)
# sub(22,2)
#
#function with return type

def mul(a,b):
    c=a*b

    print(c)
    return c

s=mul(10,2)
print(s)


# lambda function = ananomious function= function name irukadhu ana function irukum , single time usage ku aaga lambda function use panuvom

x=lambda a,b:a+b
v=x(2,5)
print(v)

#arbitrary function

# en indha function use pandrom na multiple arguments pass panalam ora timela
#munadi lam nama fixed parematers use pannom

def mularg(*args):
    total=0
    for i in args:
        total += i
    return total

s=mularg(10,2,35,8,7,2,45)
print(s)

s=20
def check():
    s=20
    print(s)
check()



