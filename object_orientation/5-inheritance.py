class Animal:
    def eat(self):
        print('eat')


#------------------------------------------------
# Animal : Parent | Base
# Mammal,Fish : Child | SUb

# class Child(Parent):

#------------------------------------------------
class Mammal(Animal):

    def walk(self):
        print('walk')

#-------------------------------------------------

class Fish(Animal):
    def swim(self):
        print('swim')

#---------- DRY -- Don't Repeat Yourself -------------

m=Mammal()
m.eat()
m.walk()
print('Mammal--> Animal',issubclass(Mammal,Animal))
f=Fish()
f.eat()
f.swim()
print('Fish--> Animal',issubclass(Fish,Animal))