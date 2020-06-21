#upper and lower string methods
spam = 'Hello World'
print(spam.upper())
print(spam.lower())
#sanitizing return input
"""answer =''
print('Do you want tot play again?')
input(answer)           # this code will fail if the player inputs YES or any other variant. 
if answer == 'yes':
    print('playing again')"""

"""answer =''
print('Do you want tot play again?')
input(answer)           # this code will sanitize the answer.
if answer.lower() == 'yes':
    print('playing again')"""
#the bolean checking of strings case state
print(spam.islower())
print(spam.isupper())
#chaining method calls
print(spam.upper().isupper())
print(spam.lower().islower())
#startswith and endswith methods
print(spam.endswith('old'))
print(spam.startswith('Hel'))
#the join method uses the string that it is called on to join the elelments of a list
print(','.join(['cats','rats', 'bats']))
print(''.join(['cats','rats', 'bats']))
print('0-0'.join(['cats','rats', 'bats']))
print('\n\n'.join(['cats','rats', 'bats']))
#The split method does the opposite ofthe Join method
print('My name is Rob'.split())
print('My name is Simon'.split('m'))
# the ljust() and rjust() functions
print('Hello'.rjust(10))
print('Hello'.ljust(20))
print('Hello'.rjust(30, '*'))
print('Hello'.ljust(30, '-'))
#the centre() method
print('Hello'.center(30, '*'))
print('Rob'.center(30, '-'))
print('Rfiojqfejrff]pefwpf'.center(30, '-'))
#stripping methods
eggs = ('Hello'.rjust(10))
print(eggs)
print(eggs.strip())
print(eggs.lstrip())
print(eggs.strip('ello'))
#The replace method
spam ='Hello there'
print(spam.replace('e', 'b'))

import pyperclip
pyperclip.copy('Hello')
print(pyperclip.paste())