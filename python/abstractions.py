# abstractions

class A:
    def __init__(self,h):
        self.speed=h

    def acceleration(self):
        self.speed += 10
        print(self.speed)


    def brakke(self):
        self.speed -= 10
        print(self.speed)


obj1=A(30)
# obj1.acceleration()
obj1.acceleration()


