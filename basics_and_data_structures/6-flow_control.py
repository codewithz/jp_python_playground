if True:
    print('Hello')
#-----------------------------------------------
x=2;

if x>3:
    print('Hello Tom')
    print('Hello Alex')

#--------------------------------------------------

a=300
b=330

if a>b:
    print(a,'is greater than',b)
else:
    print(b,'is greater than',a)

#-------------------------------------------------------

a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))

if(a>b and a>c):
    print(a,'is greater than',b,'and',c);
elif(b>a and b>c):
    print(b,'is greater than',a,'and',c);
else:
    print(c,'is greater than',b,'and',a);
#-----------------------------------------------------------
#Short Hand Operators
a=10;
b=10;

if (a==b):print(' a is equal to b')


a=11;
b=10;

print('A') if a>b else print('B')

a=50;
b=50;

print('A') if (a>b) else print('=') if a==b else print('B')

# " Don't "
# 'Don't'


