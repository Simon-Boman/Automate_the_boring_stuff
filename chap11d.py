import os
import shutil
#os walk takes in a folder as a root and traverses it, returns all files in it. so can manipulate thousands of files from a selected folder. 
# returns current folder looking at, its subfolders, and its files. 
for folderName, subfolders, filenames in os.walk('test'):
    print('The folder is ' + folderName)
    print('The subfolders (list) in ' + folderName + ' are: ' + str(subfolders))
    print('The filenames (list) in ' + folderName + ' are: ' + str(filenames))
    print()

    #can now e.g. do something for each subfolder
    for subfolder in subfolders:
        print(subfolder)
        if 'ham' in subfolder:
            #os.rmdir(subfolder)
            print('dry run, rmdir on ' + subfolder)

    for file in filenames:
        print(file)
        if file.endswith('.py'):
            #join folderName and file, i.e. recreate absolute path, and copy this to same folder BUT with new filename that has .backup at the end. 
            shutil.copy(os.path.join(folderName, file), os.path.join(folderName, file +'.backup'))  
