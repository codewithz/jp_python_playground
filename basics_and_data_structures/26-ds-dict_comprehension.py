values=[]
for x in range(5):
    values.append(x*2)

print(values)

# [expression for item in items]
values=[x*2 for x in range(5)]
print(values)

# [{key:expression for item in items}
values_dict={x:x*2 for x in range(10)}
print(values_dict)