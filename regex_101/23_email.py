import re;

word_list = ['zartab@codewithz.com','zartab.n@uni.edu','zartab-n-1312@my-company.net']


pattern='[A-Za-z0-9._]+@[A-Za-z-]+\.(com|edu|net|org)$'

for word in word_list:
    result=re.match(pattern,str(word));
    if result:
        print(f"{word} MATCHES for {pattern}")
    else:
        print(f"{word} doesn't matches for {pattern}")

