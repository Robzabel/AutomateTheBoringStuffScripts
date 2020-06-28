#! /bin/bash/python3
import re, pyperclip

# Create a regex for phone numbers
phoneRegex = re.compile(r'''(
#234-534-3421, 444-6666, (345) 324-5678, 555-000 ext 12345, ext. 23455, x58694
((\d\d\d) | (\(\d\d\d\)))?         #area code (The ? makes it optional)
(\s|-)           #first seperator
\d\d\d            #first 3 digits
-            #second separator
\d\d\d\d            #last 4 digits
(((ext(\.)?\s)|x)            #extension word part(optional)
(\d {2,5}))?         #extension number part(optional)
}''',re.VERBOSE)
# Create a regex for email addresses
emailRegex = re.compile(r""" 
# some._+thing@somewhere.com
[a-zA-Z0-9_.+]+    #namepart, have to make our own class for this one the characters dont need to be escaped becasue they are inside []
@                  #@symbol
[a-zA-Z0-9_.+]+    #domain name

""", re.VERBOSE)
# get the text off the clipboard
text =pyperclip.paste()
# extract the email/phone numbers from this text
extractedPhone=phoneRegex.findall(text)
extractedEmail=emailRegex.findall(text)

allphonenumbers = []
for phoneNumber in extractedPhone:
    allphonenumbers.append(phoneNumber[0])


print(allphonenumbers)
print(extractedEmail)
# Copy the extracted email and phone numbers to the clipboard
results = '\n'.join(allphonenumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)

