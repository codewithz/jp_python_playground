# Set --> NO DUPLICATES | UNORDERED

numbers=[1,1,2,3,4]
first=set(numbers)
uniques_clone={*first};

print('Numbers',numbers)
print('Uniques',first)

second={1,4,5}
print(second)
second.add(5)
print(second)
second.remove(4)
print(second)

print('----------- Set operations --------------------')
print("First",first)
print("Second",second)


print("Union",first | second)
print("Union",first.union(second))

print("Intersection",first & second)
print("Intersection",first.intersection(second))

print("Difference",first - second)
print("Difference",first.difference(second))

print("Symmentic Difference",first ^ second)
print("Symmentic Difference",first.symmetric_difference(second))

