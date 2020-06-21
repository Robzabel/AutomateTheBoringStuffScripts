spam = ['hello', 'hi', 'howdy', 'hey']
print(spam.index('hello'))

span = ['black', 'blue', 'green', 'yellow', 'black']
print(span.index('black'))

#printing the sort method then reversing the order
spam = [2, 4 ,7,-1, 10]
spam.sort()
print(spam)
spam.sort(reverse=True)
print(spam)
#printing the sort method in ASCII-aplphabetical then returning it in true Alphabetical
spam = ['Alice', 'Bob', 'ants', 'Cats', 'Yellow', 'badgers']
spam.sort()
print(spam)
spam.sort(key=str.lower)
print(spam)
