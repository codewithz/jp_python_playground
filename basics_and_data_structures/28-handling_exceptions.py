try:
    age=int(input("Age:"))
    print("Age is ",age)
except ValueError as ex:
    print("You didn't enter a valid age")
    print(ex)
    print(type(ex))
else:
    print('No exceptions are thrown')

print('Execution continues....')