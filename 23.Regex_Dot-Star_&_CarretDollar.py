import re
#The Caret matches to the beginning
beginsWithHelloRegex = re.compile(r'^Hello')
mo=beginsWithHelloRegex.search('Hello there')
print(mo.group())
#the Dollar character matches to the end
endsWithWorldRegex = re.compile(r'World$')
mo = endsWithWorldRegex.search('Hello World')
print(mo.group())
# you can combine the two to make the results specific
allDigitsRegex =re.compile(r'^\d+$')
mo = allDigitsRegex.search('44564546313655')
print(mo.group())
#The dot character looks for anything except a new line
atRegex = re.compile(r'.at')
print(atRegex.findall('The cat in the hat sat on the flat mat'))
#in the output only lat will be matched not Flat becasue the dot is only applicable to a single character
#the next line of code returns 1 or 2 characters that can be anything noted by the .{1,2}
atRegex = re.compile(r'.{1,2}at')
print(atRegex.findall('The cat in the hat sat on the flat mat'))
#this output will produce a space in front of the cat and mat, which we dont want

#the next example uses the * which matches 0 or one of the given criteria
name ='First name: Robert Last name: Zabel'
nameRegex = re.compile(r'First name: (.*) Last name: (.*)')
print(nameRegex.findall(name))

#Greedy/non/greedy mode examples:
serve = '<to serve humans> for dinner.>'
nongreedy = re.compile(r'<(.*?)>')
print(nongreedy.findall(serve))
#Because its got the ? it is non greedy so it stops as soon as it sees the first >
greedy =re.compile(r'<(.*)>')
print(greedy.findall(serve))
#Becasue its using greedy method it matches all the way to the last >

#The following code will match just to the first new line
prime = 'Serve the public trust.\nProtect the innocent.\nUphold the law.'
dotstar = re.compile(r'.*')
print(dotstar.search(prime))
# the following code will match all of the words and new lines
dotstar = re.compile(r'.*', re.DOTALL)
print(dotstar.search(prime))

#another example of regex methods, the ignore case method, without it the output only matches what you specify
vowelRegex = re.compile(r'[aeiou]')
print(vowelRegex.findall('Al, why does your programming book talk about robocop so much'))
#now the same example when using the IGNORECASE method
vowelRegex = re.compile(r'[aeiou]', re.IGNORECASE)
print(vowelRegex.findall('Al, why does your programming book talk about robocop so much'))