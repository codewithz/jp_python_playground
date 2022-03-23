cart=[
    ('Bread',5),('Butter',7),('Jam',4)
]


# [expression for item in items]

prices=list(map(lambda item:item[1],cart))
prices_lc=[item[1] for item in cart]
print(prices_lc)


# [expression for item in items if condition]
filtered=list(filter(lambda item:item[1]>=5,cart))
# filtered_lc=[expression for item in items if condition]
filtered_lc=[item for item in cart if item[1]>=5]
print(filtered_lc)


