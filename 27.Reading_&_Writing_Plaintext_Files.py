#first you must open the file
hellofile = open('/home/zabex/Documents/hello.txt')
#read the content and store as a variable
fileData = hellofile.read()
#Close the file after reading
hellofile.close()
#print the data from the variable
print(fileData)

hellofile = open('/home/zabex/Documents/hello.txt')
fileData = hellofile.readlines()
hellofile.close()
print(fileData)

#to open up in write mode
hellofile = open('/home/zabex/Documents/hello2.txt', 'w')
hellofile.write('hello!!!!!!!!!!!!!!!!!!!')
hellofile.close()

#to open a file in append mode
hellofile = open('/home/zabex/Documents/hello2.txt', 'a')
hellofile.write('big Blue bums')
hellofile.close()

#Writing binary Shelve files, first import the module
import shelve
shelveFile = shelve.open('/home/zabex/Documents/Shevlefile')
shelveFile['cats'] = ['Zophie', 'Pooka', 'Simon', 'Fat Tail', 'Cleo']
shelveFile.close()

#now to use the file to get the information
shelveFile = shelve.open('/home/zabex/Documents/Shevlefile')
print(shelveFile['cats'])
shelveFile.close()

#to return the keys and values
shelveFile = shelve.open('/home/zabex/Documents/Shevlefile')
print(list(shelveFile.keys()))
print(list(shelveFile.values()))