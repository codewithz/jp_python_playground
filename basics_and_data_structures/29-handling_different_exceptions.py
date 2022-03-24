try:
    age=int(input("Age:"))
    xfactor=10/age;
    numbers=[1,2]
    print(numbers[3])
except ValueError as ex:
    print("You didn't enter a valid age")
except ZeroDivisionError:
    print("You seem to entered age as 0 which is wrong")
except BaseException:
    print('Some exception occured')
else:
    print('No exceptions are thrown')

print('Execution continues....')