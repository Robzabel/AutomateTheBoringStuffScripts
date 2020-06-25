import re
#This example will show the use of the ? to match 0 or 1 times
batRegex = re.compile(r'Batman|Batwoman')
mo = batRegex.search('The Adventures of Batman')
print(mo.group())
#This Regex looks for Batman or Batwoman, the same can be achieved with:
batRegex = re.compile(r'Bat(wo)?man')
mo = batRegex.search('The Adventures of Batwoman')
print(mo.group())
#if nothing matches then the mo is filled with None:
batRegex = re.compile(r'Bat(wo)?man')
mo = batRegex.search('The Adventures of Batwowowowowooman')
print(mo == None)

#using these methods you can make a regex that looks for phone numbers that do or dont have an area code
#this first expression can only check the fully specified phone number
phoneRegex=re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneRegex.search('My phone number is 415-345-2345')
print(mo.group())
phoneRegex=re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo = phoneRegex.search('My phone number is -345-2345')
print(mo.group())

# Now we are looking at the * to match 0 or more times
batRegex = re.compile(r'Bat(wo)*man')
mo = batRegex.search('The Adventures of Batman')
print(mo.group())
mo = batRegex.search('The Adventures of Batwoman')
print(mo.group())
#so far it has done the same as the ? but if we run thelast search statement
mo = batRegex.search('The Adventures of Batwowowowowowoman')
print(mo.group())



#+ means match one or more, this code will notmatch the Batman scentece but will match the batwoman one
batRegex = re.compile(r'Bat(wo)+man')
mo = batRegex.search('The adventures of Batman')
print(mo==None)
#The wo was not present in that last search so it didnt match
mo = batRegex.search('The Adventures of Batwoman')
print(mo.group())

#An example of how you would match the characters using escapes
regex = re.compile(r'\+\*\?')
mo = regex.search('I learned about +*? regex')
print(mo.group())
#an example where it is found more than one time
regex = re.compile(r'(\+\*\?)+')
mo = regex.search('I learned about +*?+*?+*? regex')
print(mo.group())


#Matching  specific amount of times
haRegex = re.compile(r'(Ha){3}')
mo = haRegex.search('He said HaHaHa')
print(mo.group())
#This code matches the HaHaHa string because Ha appears 3 times
#you can match on a range of times as well with:
haRegex = re.compile(r'(Ha){3,5}')
mo = haRegex.search('He said HaHaHaHaHaHaHaHaHa')
print(mo.group())


#so with this code, it could match any range of 5 digits
digitRegex = re.compile(r'\d{3,5}')
mo = digitRegex.search('1234567890')
print(mo.group())
#the result is 12345 because of greedy matching, to do non greedy matching use the ?
digitRegex = re.compile(r'\d{3,5}?')
mo = digitRegex.search('1234567890')
print(mo.group())