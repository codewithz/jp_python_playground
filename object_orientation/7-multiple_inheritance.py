class Employee:
    def greet(self):
        print('Employee Greet')

class Person:
    def greet(self):
        print('Person Greet')


class Manager(Person,Employee):
    pass


#----------------------------------------

manager=Manager()
manager.greet()

#-------------------------------------------

class Flyer:
    def fly(self):
        print("Flyer")

class Swimmer:
    def swim(self):
        print("Swimmer")


class FlyingFish(Flyer,Swimmer):
    pass


f=FlyingFish()
f.fly()
f.swim()