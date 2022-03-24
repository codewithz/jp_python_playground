numbers=[3,51,2,8,6]
print('Original',numbers)

numbers.sort()
print('Sorted',numbers)
print('Original',numbers)

numbers.sort(reverse=True)
print('Reverse Sorted',numbers)
print('Original',numbers)

otherNumbers=[43,1,67,23,54]
print('Original others',otherNumbers)

sortedList=sorted(otherNumbers);
print("sorted Other List",sortedList)
print('Original others',otherNumbers)

reverse_sorted_list=sorted(otherNumbers,reverse=True);
print("Reverse Sorted Other List",reverse_sorted_list)
print('Original others',otherNumbers)

#-------------------------------------------------------------
print('---------------- Complex Object--------------')

cart=[
    ('Bread',5),('Butter',7),('Jam',4)
]

def sort_cart(item):
    return item[1]

print('Cart',cart)
cart.sort(key=sort_cart);
print('Sorted Cart',cart)

cart.sort(key=sort_cart,reverse=True);
print('Reverse Sorted Cart',cart)
