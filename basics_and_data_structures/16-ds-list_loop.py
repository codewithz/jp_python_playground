letters=["a","b","c","d"]

for letter in enumerate(letters):
    print(type(letter))
    print(letter[0],letter[1])


# item=(0,'a');
# index,letter=item;


print('-------------------------------')

for index,letter in enumerate(letters):
    print(index,letter)

print('--------------------------')

testList=[['a','b'],['c','d']]

for index,element in enumerate(testList):
    print('Iterating through List #',index+1)
    for index,letter in enumerate(element):
        print(index,letter)