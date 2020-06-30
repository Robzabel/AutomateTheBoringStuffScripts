#import the shell utilities module
import shutil
#this next line demonstraits how to copy the file and rename it at the same time
shutil.copy('/home/zabex/Documents/hello2.txt','/home/zabex/Downloads/CopiedFile1.txt')
#copy a whole folder
shutil.copytree('/home/zabex/Downloads', '/home/zabex/Desktop/DownloadsBackipFolder')
#move a folder
shutil.move('location and file name source', 'location and file name destination')
#rename a file
shutil.move('name of file you want to rename', 'the name you want to give it')

import os
#Delete a single file
os.unlink('/home/zabex/Downloads/CopiedFile1.txt')
#Delete an entire empty directory
"""os.rmdir('directory path')"""
#To remove a directory that has stuff in
shutil.rmtree('/home/zabex/Desktop/DownloadsBackipFolder')

import send2trash
send2trash.send2trash('/home/zabex/Documents/hello.txt')