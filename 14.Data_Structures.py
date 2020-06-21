cats = { 'name': 'fenty', 'age': 6, 'colour': 'black'} # this creates a dictionary of information on the cat
allCats = [] #this creates a blank dictionary that can hold all data about all cats in the variable called allCats
allCats.append(cats)
allCats.append({ 'name': 'Pooka', 'age': 3, 'colour': 'grey'})#Adding data to the variable allCats
allCats.append({ 'name': 'Sweaty', 'age': 4, 'colour': 'blue'})
allCats.append({ 'name': 'John', 'age': 5, 'colour': 'orange'})
print(allCats) #this prints the data structure all cats

#a simple tic tac toe board game
import pprint

theBoard = {'top-L':' ', 'top-M': ' ', 'top-R': ' ', \
'mid-L':' ', 'mid-M': ' ', 'mid-R': ' ', \
'low-L':' ', 'low-M': ' ', 'low-R': ' ',}#this creates the board as a data structure
pprint.pprint(theBoard)

#write a function that outputs the board in a nice display
def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-----')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-----')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
printBoard(theBoard)# this prints the board as you can see you have the makings of a tic tak toe game

#some examples of using the type function
print(type(42))
print(type('hello'))
print(type(theBoard))