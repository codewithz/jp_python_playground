try:
    with open("1-hello.py") as file, open('2-dataypes.py') as target:

        x=10/0;
        print('Operation with file opened')

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
    print("File Closed",file.closed)
    print(file)
    file.close()
    target.close()
    print('File is closed')

print('Execution continues....')