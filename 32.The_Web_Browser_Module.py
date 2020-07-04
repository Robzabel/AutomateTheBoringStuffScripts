#!/usr/bin/python3
import webbrowser, sys,pyperclip
#webbrowser.open('https://www.google.co.uk')
sys.argv
# check if cli arguments were passed
if len(sys.argv) > 1:
    address =' '.join(sys.argv[1:]) # write a join statement that takes a slice of the arguments passed to the programme but cuts out the program name
else:
    address = pyperclip.paste()

#the URL to go to would be https://www.google.co.uk/maps/place/(our address variable)
webbrowser.open('https://www.google.co.uk/maps/place/' + address)

