myCat = {'size': 'fat', 'colour': 'black', 'disposition': 'loud'}
print(myCat['size'])

#order doesnt matter with dictionarys
print([1,2,3,] == [3,2,1,])
#with a list this eveluates to false becasue the values are not in the correct order

eggs = {'name': 'Robert', 'species': 'cat', 'age': 8}
ham = {'age': 8, 'species': 'cat','name': 'Robert'}
print(eggs == ham)
#this evaluates to true even tho the order is different becasue Dictionaries are unordered.
print('name' in eggs)
print('carrot' not in ham)
#the methods that can be used for lists:
#find the keys and display in a list format:
print(list(eggs.keys()))
#find the values and display in a list format:
print(list(eggs.values()))
#then find the items which is printed in a list format but returns the values in tuples@
print(list(eggs.items()))
#if you dont use the list function, the data is returned in a dictionary data type as seen here:
print(eggs.keys())
#these methods can kbe used in for loops:
for k in eggs.keys():
    print(k)
for v in eggs.values():
    print(v)
for i in eggs.items():
    print(i)
for k, v in eggs.items():
    print(k,v)

#the get method example, this looks for age in the eggs dict, if it doesnt find it, a 0 will be returned
print(eggs.get('age', 0))
print(eggs.get('car', 80085))


#if we didnt have the set default method, you would have to write out code like this:
if 'colour' not in eggs:
    eggs['colour'] = 'black'
print(eggs)
#to save all this code, it can be done in a one liner:
eggs = {'name': 'Robert', 'species': 'cat', 'age': 8}
eggs.setdefault('colour', 'black')
print(eggs)
eggs.setdefault('colour', 'Orange')
print(eggs) #The colour doesnt change to orange because the colour black already exists

#a quick programme to count the number of times a letter appears in a string

message = 'It was a bright colsd day in April and the clocks were striking thirteen'
count = {} #this sets the count variable to a dictionary data type
#make a for loop to run through the message
for character in message:#this makes the program look at each character in the string.
    count.setdefault(character, 0) # this makes sure that every letter has the value of 0 if it has not been added to count already
    count[character] = count[character] +1 # this adds one for every time the character appears
print(count)
count = {}
for character in message.upper():#this makes the program look at each character in the string, in this version all character are turned uppercase for more accurate count
    count.setdefault(character, 0) # this makes sure that every letter has the value of 0 if it has not been added to count already
    count[character] = count[character] +1 # this adds one for every time the character appears
print(count)

import pprint #here we import pretty print module
count = {}
for character in message.upper():#this makes the program look at each character in the string, in this version all character are turned uppercase for more accurate count
    count.setdefault(character, 0) # this makes sure that every letter has the value of 0 if it has not been added to count already
    count[character] = count[character] +1 # this adds one for every time the character appears
pprint.pprint(count) #this time pprint is called which will give  much nicer output of the dictionary