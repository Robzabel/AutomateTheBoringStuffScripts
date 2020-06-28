# creating a file path from a list:
print('\\'.join(['Folder1', 'folder2', 'folder3', 'image.pmg']))
#I would be fucked if i hard coded this because i use linux and this is a Windoes paths style
#To make a directory path with the module from os
import os
print(os.path.join('foler1', 'folder2', 'folder3', 'image.png'))
print(os.sep)
#get the current working directory from the os module
print(os.getcwd())
os.chdir('/home/zabex/Desktop')
print(os.getcwd())

#shows what the abslute path would be of any file passed as an argument
print(os.path.abspath('spam.png'))
print(os.path.abspath('../../spam.png'))

#returns true or false if the argument is an absolute path or not
print(os.path.isabs('spam.png'))
print(os.path.isabs('/home/zabex/Desktop/spam.png'))

#find the relative path between two paths
print(os.path.relpath('/folder1/folder2/spam.png', '/Folder1'))

#Pull the directory name or the filename from a path
print(os.path.dirname('/home/zabex/Desktop/spam.png'))
#pull the last part of the path
print(os.path.basename('/home/zabex/Desktop/spam.png'))

#find if a file exists in a certain directory
print(os.path.exists('/home/zabex/Desktop/spam.png'))

#chek if the path ends on a directory  or a file
print(os.path.isfile('/home/zabex/Desktop/spam.png'))
print(os.path.isdir('/home/zabex/Desktop/spam.png'))

#check the size of a file and list a directory
print(os.path.getsize('/home/zabex/Downloads/outOfHours.wav'))
print(os.listdir('/home/zabex/Downloads'))

# a small program to find the size of all the files within a directory
totalsize = 0   #initialise the variable

for file in os.listdir('/home/zabex/Downloads'): #start the loop on the directory items
    if not os.path.isfile(os.path.join('/home/zabex/Downloads', file)): #check that folders in the dir are not counted, have to use the absolute path or it wont know where to look
        continue
    totalsize += os.path.getsize(os.path.join('/home/zabex/Downloads', file)) #almost right just make sure to put absolute path
print(totalsize)

#to create a new directory
os.makedirs('/home/zabex/Downloads/Testing123')
os.rmdir('/home/zabex/Downloads/Testing123')