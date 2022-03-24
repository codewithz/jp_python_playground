try:
    file=open("1-hello.py")
    age=int(input("Age:"))
    xfactor=10/age;

except ValueError as ex:
    print("You didn't enter a valid age")

except ZeroDivisionError:
    print("You seem to entered age as 0 which is wrong")

except BaseException:
    print('Some exception occured')
else:
    print('No exceptions are thrown')
finally:
    file.close()
    print('File is closed')

print('Execution continues....')