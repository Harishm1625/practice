
# constructor

class A:
    def __init__(self,name,year):
        self.n=name
        self.y=year

    def car(self):
        print(self.n,self.y)

obj=A("tuv",2021)
obj.car()

class B:
    def __init__(self,name,mark):
        self.n=name
        self.m=mark
    def  details(self):
        print(self.n,self.m)

    def cls11(self):
        print(self.n,self.m)

    def cls12(self):
        print(self.n, self.m)


cls=B("harish",45)
cls.details()

cls=B("jai",20)
cls.details()

cls1=B("kumar",33)
cls1.cls11()

cls2=B("tharun",75)
cls2.cls12()

#  inga enna pandrom na ora time mattum global ha variable ha declare pandrom
#  same function use pani different values hum pass panalam
# next different different function ku same variable assign panikulam
# aprm object la poitu namaku thevapadra values assign panikulam

