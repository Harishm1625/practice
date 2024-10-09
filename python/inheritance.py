# inheritence

#  single in heritance

class BaseClass:
    def method1(self):
        print("BaseClass la irukkira method")

class DerivedClass(BaseClass):
    def method2(self):
        print("DerivedClass la irukkira method")

# example -- idhu vandhu object name nama object vachu than call pananum

example=DerivedClass()

example.method1()


# multiple inheritance--more than 2 classes ha pass panalam

class Parent1:
    def method1(self):
        print("Parent1 la irukkira method")

class Parent2:
    def method2(self):
        print("Parent2 la irukkira method")

class Child(Parent1, Parent2):
    def method3(self):
        print("Child class la irukkira method")

child_instance = Child()
child_instance.method1()  # Parent1 la irukkira method
child_instance.method2()  # Parent2 la irukkira method








# multi level inheritence

# mks oru parent class - andha parent class ha hbt ku paremeter ha pass pandrom
# ipo mks la irukaradhu hbt ku equal aaidum
# aprm hbt ha bls ku pass pandr apo mks la irukaradhum hbt la irukaradhum bls ku vandhurum

class mks:
    def owner(self):
        print("lorry")

class hbt(mks):
    def sons(self):

        print("my sons")
class bls(hbt):
    def v3(self):
        print("family")

kum=bls()
kum.owner()
kum.sons()
kum.v3()

# Hierarchical Inheritance

class Parent:
    def method_parent(self):
        print("Parent la irukkira method")

class Child1(Parent):
    def method_child1(self):
        print("Child1 la irukkira method")

class Child2(Parent):
    def method_child2(self):
        print("Child2 la irukkira method")

child1_instance1 = Child1()
child1_instance2 = Child2()

child1_instance1.method_parent()  # Parent la irukkira method
child1_instance1.method_child1()
child1_instance2.method_parent()
child1_instance2.method_child2()



# Example of Hybrid Inheritance
class Grandparent:
    def method_grandparent(self):
        print("Grandparent la irukkira method")

class Parent1(Grandparent):
    def method_parent1(self):
        print("Parent1 la irukkira method")

class Parent2(Grandparent):
    def method_parent2(self):
        print("Parent2 la irukkira method")

class Child(Parent1, Parent2):
    def method_child(self):
        print("Child la irukkira method")

# Usage
child_instance = Child()
child_instance.method_grandparent()  # Inherited from Grandparent
child_instance.method_parent1()       # Inherited from Parent1
child_instance.method_parent2()       # Inherited from Parent2
child_instance.method_child()          # Child's own method



