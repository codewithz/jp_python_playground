
message="Hello All"

def greet(name):
    global  message
    message='Hello'

def send_email(name):
    message='Hi'


print(message)
greet('Zartab')
print(message)
#--------------------Python doesn't suppot block scope-------
for number in range(3):
    print(number)

print('---',number)