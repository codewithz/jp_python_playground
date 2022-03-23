cart=[
    ('Bread',5),('Butter',7),('Jam',4)
]

# def sort_cart(item):
#     return item[1]

sorting_key=lambda item:item[1];

print('Cart',cart)
cart.sort(key=lambda item:item[1]);
print('Sorted Cart',cart)

cart.sort(key=sorting_key,reverse=True);
print('Reverse Sorted Cart',cart)


#-----------------------------------------------------

prices=[]

for item in cart:
    prices.append(item[1])

x=list(map(lambda item:item[1],cart))

print(x)
print("Prices",prices)

#--------------------------------------------------------

filtered_list=[]

for item in cart:
    if(item[1]>=5):
        filtered_list.append(item)

print('Filtered Items',filtered_list)

f_list=list(filter(lambda item:item[1]>=5,cart))

print(f_list)

#----------------------------------------------------
import functools;

total_amount=functools.reduce(lambda acc,value:acc+value,prices);

print('Total Value',total_amount)