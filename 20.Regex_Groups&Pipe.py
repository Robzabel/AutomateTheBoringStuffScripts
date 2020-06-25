#using regex to find phone numbers

# To find the whole phone number
import re
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 223-433-2345')
print(mo.group())
#to find differernt groups of the text
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo2 = phoneNumRegex.search('My number is 223-433-2345')
print(mo2.group(1))
print(mo2.group(2))
#to find parentheses in the text you must escape them in the regex search
phoneNumRegex = re.compile(r'\(\d\d\d\) \d\d\d-\d\d\d\d')
mo3 = phoneNumRegex.search('My number is (223) 433-2345')
print(mo3.group())
#Using pipes to retun many values with one search
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group())
#to find which value was matched:
print(mo.group(1))