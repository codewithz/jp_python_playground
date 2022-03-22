letters=["a","b","c"];
print('Original',letters)


# Add
letters.append('d')
print('Append',letters)


letters.insert(0,'-')
print("Insert",letters)

# remove

letters.pop(0)
print('Pop',letters)

letters.remove("b")
print('Remove',letters)

del letters[1]
print('del',letters)

del letters[1:3]
