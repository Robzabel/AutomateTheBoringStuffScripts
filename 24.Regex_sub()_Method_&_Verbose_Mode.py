import re
#This code looks for the names of the secret agents
namesRegex = re.compile(r'Agent \w+')
print(namesRegex.findall('Agent Alice gave Agent Bob the secret documents.'))
# use the sub() to substitute the output
print(namesRegex.sub('REDACTED', 'Agent Alice gave Agent Bob the secret documents.'))
#to make the output a bit fancyer we can do this:
namesRegex = re.compile(r'Agent (\w)\w*')
print(namesRegex.findall('Agent Alice gave Agent Bob the secret documents.'))
#this find all call returns just the Letter A and B becasue it only returns the group objects
#the A comes becsue Agent (A)lice is the matching criteria. \w+ stops when it hits the space because we
#have not told it to match for that, same with the B in Bob

#To replace the names of the agents but show the first letter you use the following
namesRegex = re.compile(r'Agent (\w)\w*')
print(namesRegex.sub(r'Agent \1*****', 'Agent Alice gave Agent Bob the secret documents.'))

#verbose does not count white space
phoneNumberRegex = re.compile(r"""
\d\d\d    #area code
-         #first dash
\d\d\d    #first 3 digits
-         #second dash
\d\d\d\d  #Last 4 digits """, re.VERBOSE)


#using the re.arguments
sampleRegex = re.compile(r'[aeiou]  {2}', re.I | re.DOTALL | re.VERBOSE)
print(sampleRegex.findall('Hello I am an Eel'))