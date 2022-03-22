print('---------------------Normal Function------------')

def greet():
    print('Hi There')
    print('Welcome Aboard')


greet()

#---------------------------
print('--------------------- Function with Arguments------------')
def greeting(first_name,last_name):
    print(f'Hi {first_name} {last_name}')
    print('Welcome Aboard')


greeting('Zartab','Nakhwa')
greeting('John','Smith')
#---------------------------
print('---------------------Functions with return type------------')
#types of function

# 1 - Performs a Task

def greet(name):
    print(f"Hello {name}")

greet('Zartab')

# 2- Returns a Value
def get_greeting(name):
    return f"Hi {name}"

message=get_greeting('Tom')
# Send this in an email
#Store it in a file
# Store it in a DB
# Send over network
print(message)



#---------------------------
print('---------------------Keyword Arguments------------')

def increment(number,by):
    addedValues=number+by;
    return addedValues;


result=increment(by=1,number=2)
print(result)


def formatMyWay(first_name,last_name):
    return f"{first_name.upper()} {last_name.lower()}"

result=formatMyWay(last_name='Nakhwa',first_name='Zartab')
print(result)
#---------------------------
print('---------------------Default Arguments------------')

def incrementNumbers(number,by=1):
    return  number+by;


result=incrementNumbers(7)
print(result)
result1=incrementNumbers(7,4)
print(result1)

#---------------------------

print('---------------------Varying Arguments [xargs]------------')

def multiply(*numbers):
    print(numbers,type(numbers))
    total=1
    for number in numbers:
        total=total*number
    return total

# (2, 3, 4, 5, 6)
#  [] - list
#  () - tuple [read only list]
result=multiply(2,3,4,5,6)
print(result)

def someTest(*names):
    for name in names:
        print(name)


someTest('Zartab','tom','Alex')
#---------------------------
print('---------------------Varying Arguments for Dict [xxargs]------------')

def save_user(**user):
    print(user)
    print(type(user))


save_user(id=1,name="tom",salary=45098.4)


# #---------------------------




# def multiply(x,y):
#     return 10
#
# def multiply(x,y,z):
#     return x+y+z;
#
# print(multiply(1,2))
# print(multiply(1,2,3))
















#---------------------------
# s1='Hello'
# s2='Hello'
#
# x=s1 is s2;
# print(x)