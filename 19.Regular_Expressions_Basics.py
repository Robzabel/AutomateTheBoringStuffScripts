#non regular expression
def isPhoneNumber (text):
    if len (text) != 12:
        return False #not phone number sized
    for i in range (0, 3):
        if not text[i].isdecimal():
            return False # no area code
    if text[3] != '-':
        return False # Missing Dash
    for i in range (4, 7):
        if not text[i].isdecimal():
            return False # no first 3 digits
    if  text[7] != '-':
        return False # Missing second dash
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False #missing last 4 digits
    return True

message = 'Call me 333-443-5349 or at 246-765-3432'
foundNumber = False
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
        foundNumber = True
if foundNumber == False:
    print('couldnt find any phone numbers')

#now to do the same thing with regular expressions
import re
message = 'Call me 425-555-1011 tomorrow, or 123-456-7891'

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search(message)
print(mo.group())