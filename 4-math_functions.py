import math;


i=10;
print(type(i))

f=23.7
print(type(f))

c=10+5j;
print(type(c))

# COnverting the types of this variables
f1=float(i)
print(i)
print(f1)

i1=int(f);
print(f)
print(i1)

c1=complex(f)
print(f)
print(c1)

# Inbuilt Math Functions

minValue=min(1,2,3,4,5,6,0,10)
print('Min value is',minValue)

maxValue=max(1,2,3,4,5,6,0,10)
print('Max value is',maxValue)

a=-3
print("O:",a)

a=abs(a);
print("Abs",a)

cubeOfFour=pow(4,3);
print('4 to the poweer of 3 is',cubeOfFour)

# Math Module

print(dir(math))

print(math.pi)

squareRoot=math.sqrt(64)
print('Square Root of 64 is',squareRoot)

print("If we divide 5 with 2, remainder will be",math.remainder(9,6))

number=3.4

print("Floor Value is",math.floor(number));
print('Cieling Value is',math.ceil(number))

number=4;

factorialOfFour=math.factorial(number);
print('Factorial of 4 is',factorialOfFour)

# Trignometry  Functions

rad=math.radians(90)

print('Radian of 90 is',rad)

print('Sin 90:',math.sin(math.radians(90)))
