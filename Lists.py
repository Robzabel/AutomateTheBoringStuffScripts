spam =['cat', 'bat', 'rat', 'elephant']

print(spam[0])
print(spam[1])          #Printing the bog standard list
print(spam[2])
print(spam[3])

eggs = [['cat', 'bat'], [10, 20, 30, 40, 50]]

print(eggs[0][0])
print(eggs[0][1])
print(eggs[1][0])       #Printing the list with 2 indexes
print(eggs[1][2])
print(eggs[1][3])
print(eggs[1][4])


print(eggs[1][-1])
print(eggs[1][-2])
print(eggs[1][-3])
print(eggs[1][-4])      #Prinitng the list with 2 indexes in reverse order
print(eggs[1][-5])
print(eggs[0][-1])
print(eggs[0][-2])

thisIsaSliceofSpam = spam[1:3]
print(thisIsaSliceofSpam)   #This shows how to take a slice



new = [10, 20, 30]
print(new)
new[1]= 'hello'         #this shows how to assign a value to a list using the index
print(new)

new[1:3] = ['CAT', 'DOG', 'MOUSE']  #this shows hoe to assign values of a list using a slice.
print(new)

print(new[:4])          #Demonstration of slice shortcuts
print(new[0:])


del new[1]          #demonstration of the unassignment (del) statement
print(new)

print(len(new))     #Using the len function to return the amount of items in a list
print(len([1,2,3]))

number1 = [1,2,3]
number2 = [4,5,6]
number3 = number1 + number2     #Examples of using the + operator to concatenate the lists
print(number3)
print([1,2,3] + [4,5,6])

print(new * 3)      #Example using the mulitiplication operator to print the list 3 times


print(list('Hello World'))  #Example of using the list function to create a list from a string

howdy = "howdy"
listNew = [ 'hello', 'Wosson', 'Yea you', 'howdy']  #example of using the in/not in operators to return true or false values, needs to go in interactive shell
"howdy" in 'hello', 'Wosson', 'Yea you', 'howdy'