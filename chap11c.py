# copy and move files and folders
import shutil

#copy file from, to
shutil.copy('E:\\kod\Automate_the_boring_stuff\\bacon.txt', 'E:\\kod\Automate_the_boring_stuff\\test')

#copy and rename
shutil.copy('E:\\kod\Automate_the_boring_stuff\\bacon.txt', 'E:\\kod\Automate_the_boring_stuff\\test\\baconbaconbacon.txt')

#copy folder
#shutil.copytree('E:\\kod\Automate_the_boring_stuff\\test', 'E:\\kod\Automate_the_boring_stuff\\test_backup')

#move file to new location
#shutil.move('E:\\kod\Automate_the_boring_stuff\\hello.txt', 'E:\\kod\Automate_the_boring_stuff\\test2')

#cant rename, but can do move to same folder!
#shutil.move('E:\\kod\Automate_the_boring_stuff\\hello2.txt', 'E:\\kod\Automate_the_boring_stuff\\helloRenamed.txt')


#deleting files and folders
# NOTE - PERMANENTELY DELETES - DOES NOT SEND IT TO THE RECYCLING BIN!!!!
import os
#permanentely deletes file. can use relative like here, or absolute path to be sure
#os.unlink('delete.txt')

#remove directory - folder must be empty! 
#os.rmdir('deleteFolder')

import shutil
#permanentely deletes folder AND its contents
#shutil.rmtree('deleteFolderWithFiles')

#Dry Run to be safe of what you delete...
#dry run - comment out the actual calls to delte functions, just print and test if e.g. typo
for filename in os.listdir():
    if filename.endswith('.txt'):
        #os.unlink(filename)
        print(filename)

#send2trash module - instead of deleting permanentely, sends to your recycling bin! 
import send2trash

send2trash.send2trash('sendtotrash.txt')