letters=["a","b","c","d"]

print(letters.index("a"))

# Way 1- to make sure if element is not found, program doesn't break
if "d" in letters:
    print(letters.index("d"))

# Way 2- to make sure if element is not found, program doesn't break
count=letters.count("d");

if count>0:
    print(letters.index('d'))

