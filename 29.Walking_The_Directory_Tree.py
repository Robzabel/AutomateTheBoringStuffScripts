import os
for folderName, subfolders, filenames in os.walk('/home/zabex/FolderWalk'):
    print('The folder is ' + folderName)
    print( 'The subfolders in %s are %s' % (folderName, subfolders))
    print('The filenames in %s are: %s' % (folderName, filenames))
    print()