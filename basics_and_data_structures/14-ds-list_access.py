letters=["a","b","c","d"]
print(letters)
# Access the first
print(letters[0])

#  Access the last
print(letters[-1])

# Change the value in the list
letters[0]='A'

print(letters)

#Accessing in Ranges
print(letters[0:2])

print(letters[:3])
print(letters[1:])
# Printing the list as well as cloning
print(letters[:])
print('-----------------------')
# Steppers in List
numbers=list(range(20))

print(numbers[::2])

print(numbers[::-1])
