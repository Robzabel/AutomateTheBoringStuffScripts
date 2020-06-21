print(list ('hello'))
name = 'Robert'
print(name[4])
print(name[1:3])

answer = 'Rob' in name
print(answer)

#Modifying an immutable string:
name = 'Zophie a Cat'
newName = name[0:7] + 'the' + name[8:12]
print(newName)

#assigning variables
name='Jason'
othername = name
print(othername) # this prints Jason becasue you put the value held in name into the memory location of othername

list1 = [ 1, 2, 3, 4,]
list2 = list1
list2[1] = 'Hello'
print(list2)
print(list1)
# Both lists were changed because the varables reference the list but do not hold the data in memory because it its a mutable object
#they are basically just pointers to the list somewhere in memory


#even though the append function happens to the local variable of the list, it affects the global list too
def eggs(paramater):
    paramater.append('Hello')

spam = [1, 2, 3]
eggs(spam)
print(spam)

#Import the copy module and use the function deep copy to make 2 instances of the same list
import copy
spam = ['a', 'b', 'c', 'c']
cheese = copy.deepcopy(spam)
spam.append('hello')
print(spam)
print(cheese)

#an example of list continuation
spam = ['apples',
        'oranges',
        'dogs',]
#another example of line continuation with the baclslash special character
print('my cat Fenty '\
      'is a giant pain' \
      ' in the ass')