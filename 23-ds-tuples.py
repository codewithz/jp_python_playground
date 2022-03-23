#Tuples are read only lists

# Ways of declaring a Tuple

point=(1,2)
print(type(point))
print(point)

point=1,2
print(type(point))
print(point)


point=1,
print(type(point))
print(point)

point=(1,2)+(3,4)
print(type(point))
print(point)

point=(1,2)*3
print(type(point))
print(point)

point=tuple([1,2])
print(type(point))
print(point)


##-----------------------------------------------------

point=(1,2,3)

print("Range Access:",point[0:2])

x,y,z=point

print('X:',x);
print('Y:',y);
print('Z:',z);

if 10 in point:
    print('Exists')

#--------------------------------------------

point[0]=20;