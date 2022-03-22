for number in range(3):
    print('Attempt',number+1,(number+1)*'.')

print("---------------------------")

for number in range(1,4):
    print('Attempt',number,(number)*'.')

# print('#'*20)

#------------------------------------------------------------
print('--------------------------------------')
# for..else

successful=False

for number in range(1,6):
    print("Attempting to send message");
    if number==2 and successful:
        print('Successfully sent the message.')
        break
else:
    print('Attempted for 5 times and failed')
print('--',number)
#Else block will be activated if the for loop doesn't end early

#----------------------------------------------------------------
print('----------------------------------------------------')
# Nested Loop
# (0,0)
# (0,1)
# (0,2)
# (1,0)
#(1,1)

for x in range(5):
    for y in range(3):
        print(f"({x},{y})")
        # print("(",x,",",y,")")

first_name='Zartab'
last_name='Nakhwa'

print(f"Hello {first_name} {last_name}")