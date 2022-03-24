import random
import string

print(random.random())

print(random.randint(1,10))

print(random.choice([1,2,3,4]))

print(random.choices([1,2,3,4],k=2))


print("".join(random.choices("abcdefghij",k=4)))


print("".join(random.choices(string.ascii_lowercase+string.ascii_uppercase+string.digits,k=4)))

