name='Zartab'
print(name)

print(dir(name))

# Multi Line String

paragraph="""
India is my country
All Indians are my brothers and sisters
I love my country
"""

print(paragraph)

paragraph='''
India is my country
All Indians are my brothers and sisters
I love my country
'''

print(paragraph)

"""

This can also be considered 
as multi line comment

"""

# this is
# a multi
# line comment

## String are arrays

word='kitkat';

print(word[1]);

print(word[0:4])

print(word[1:3])

print(word[-5])

print(word[-6])

# print(word[-7])

print(word[-5:-2])


print(word[-2:-5])

print(word[0:20])

print(word[3:])
# print(word[7])


# Task

word='Internationalization';

print(word[-15:-9])
print(word[-15:11])

# Length of a String

print(len(word))


#Trimming --> strip()

wordWithSpaces="   Hello World   ";
print(len(wordWithSpaces))
print(wordWithSpaces)

wordWithSpaces=wordWithSpaces.strip()
print(len(wordWithSpaces))
print(wordWithSpaces)

# Casing

company='jp morgan'
print("Company:",company)

company=company.upper();
print("Company:",company)

sentence='IT IS AN IMPORTANT CONCEPT';
print(sentence)
sentence=sentence.lower()
print(sentence)

sentence='i am happy to be here';
print(sentence)
sentence=sentence.capitalize()
print("Capitalize:",sentence)

sentence='i am happy to be here';
print(sentence)
sentence=sentence.title()
print("Title:",sentence)

#Replacement

language='Jxvx';
print(language)

language=language.replace('x','a')
print(language)

someText='Jxvx';
print('O:',someText)

someText=someText.replace('x','a',1);
print('U:',someText)

#Split a String

line="1,Tom,Dev,IT,30000";
print("O:",line);
data=line.split(",");
print(data)
print(type(data))

# in keyword

line='My name is Tom';

checkTom="Tom" in line;
print("Is Tom in line:",checkTom)

checkALex="Alex" in line;
print("Is Alex in line:",checkALex)

# Format Method

line="My name is Zartab, I am {} years old";

age=31

fline=line.format(age);

print(fline)

line="My name is {}, I am {} years old";

name="Micheal";
age=35;

fline=line.format(name,age)
print(fline)

# Numbered Formatting
line=" I am a  {0}, I train my {1}, {1} asks doubts to {0}"

fline=line.format("Trainer","Trainee")
print(fline)

# Named Formatting

line="Hey, I am a trainer, my name is {trainer}, my trainee name is {trainee},{trainee} ask doubts to {trainer}"

fline=line.format(trainee='Tom',trainer='Zartab');
print(fline)


# Count

name='Zartab';

aCount=name.count('a');

print('Count of a:',aCount)

# Starts with and endsWith

print("Starts with Z",name.startswith('Z'));

print('Ends with Z',name.endswith('z'))

#
# # Escape Character
# \n - new line
# \t - tab
# \\ - backslash
# \" - double quotes

# text="This is a backslash ( \ )";
# print(text)

text="This is a backslash \\";
print(text)

text="These are two backslashes \\\\";
print(text)

text=" I work at \"JP MORGAN\""
print(text)