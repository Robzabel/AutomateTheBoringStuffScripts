import re
#this returns a list because there are no regular expression objects to match with
resume = """ Lorem ipsum dolor sit amet, consectetur 555-777-8888adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
Duis aute irure dolor in 234-321-2467 reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
Excepteur sint occaecat cupidatat non proident,333-444-5555 sunt in culpa qui officia deserunt mollit anim id est laborum."""
phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
print(phoneRegex.findall(resume))

#this next block of code will return a list of tuples because we have specified regex objects to match with
resume = """ Lorem ipsum dolor sit amet, consectetur 555-777-8888adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
Duis aute irure dolor in 234-321-2467 reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
Excepteur sint occaecat cupidatat non proident,333-444-5555 sunt in culpa qui officia deserunt mollit anim id est laborum."""
phoneRegex = re.compile(r'((\d\d\d)-(\d\d\d-\d\d\d\d))')
print(phoneRegex.findall(resume))

#example of character calss matchings
lyrics = """1 partridge in a pear tree, 2 turtle doves, 3 french hens, 4 calling birds, 5 gold rings, 6 geese a-laying, \
7 swans a-swimming, 8 maids a-milking, 9 ladies dancing, 10 lords a-leaping, 11 pipers piping, 12 drummers drumming"""
#this uses the srtandard shorthand regex to match the criteria,
#this basically says match for 1 digit or more then a space then one workd or more
xmas=re.compile(r'(\d+\s\w+)')
print(xmas.findall(lyrics))
#the output stops after the first wrod becasue we have nottold it to tmatch the next space and the following words
#to fix thatt we can do this :
xmas=re.compile(r'(\d+\s\w+\s\D+)')
print(xmas.findall(lyrics))

#you can also define your own character cases to match criteria
#this character class will match vowels in the text:
vowelregex = re.compile(r'[aeiouAEIOU]')
print(vowelregex.findall('local cop eats baby food'))
#to make it match only when there are 2 vowels nest to each other we can use:
doublevowel = re.compile(r'[AEIOuaeiou]{2}')
print(doublevowel.findall('Robocop eats baby food'))
#to make the matching criteria a negative as in match if the following is not present, use a carrot
vowelregex = re.compile(r'[^aeiouAEIOU]')
print(vowelregex.findall('local cop eats baby food'))