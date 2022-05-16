import os

#need to add \ to escape the backslash, so \\ in string is actual backslash. or use rawstring.
print('\\')
print(r'c:\spam\eggs.png')
path = 'c:\\spam\\eggs.png'
print(path)

#create filepath by joining individual folders and file on \ - only works for windows tho! 
filepath = '\\'.join(['folder1', 'folder2', 'folder3', 'file.png'])
print(filepath)

#module os can be used! 
#the os.path.join works for all OS's, returns for appropriate OS you are running on. 
filepath = os.path.join('folder1', 'folder2', 'folder3', 'file.png')
print(filepath)

#get current working directory - where the current program is running from (What folder)
print(os.getcwd())
# so if we give some file path, like 'spam.png', without any more path to it, python will assume that it can be found in the current working directory. 

# os.chdir() - change current working directory
os.chdir('c:\\')
print(os.getcwd())
# now, if we did some function e.g. deleteFile('spam.png') - python will now assume the file canbe found in the current working directory, i.e. the root folder. 


#Absolute vs relative paths.
# e.g. 'spam.png' is a relative file path. Relative to the current working directory!  
# relative file path can also begin with other folders, e.g. 'folder1\\folder2\\spam.png' - will then assume that folder1 is inside root folder. 
# absolute path always begins with complete location of a program, and begins with root. E.g. r'E:\kod\Automate_the_boring_stuff\spam.png'

# . and .. folders. 
# . stands for this directory, dont need to specify .\, i.e. can do either .\nextfolder\file.txt ; or nextfolder\file.txt 
#  .. stands for parent folder. 

os.chdir(r'E:\kod\Automate_the_boring_stuff')
print(os.getcwd())
print('')

# path.abspath gives absolute path of file
print(os.path.abspath('chap11a.py'))
print(os.path.abspath('..\\filename.txt'))

# path.isabs returns true if is absolute path or not, i.e. begins with root folder
print(os.path.isabs('chap11a.py'))
print(os.path.isabs('..\\filename.txt'))
print(os.path.isabs('E:\\kod\\Automate_the_boring_stuff'))

# path.relpath - gives you relative path between 2 paths you give it. endpath, startpath. 
print(os.path.relpath('E:\\kod\\Automate_the_boring_stuff\\chap11a.py', 'E:\\kod\\')) 


#pull of directory name, or base name. 
print(os.path.dirname('E:\\kod\\Automate_the_boring_stuff\\chap11a.py'))
print(os.path.basename('E:\\kod\\Automate_the_boring_stuff\\chap11a.py'))
print(os.path.basename('E:\\kod\\Automate_the_boring_stuff'))


#check if file exists
print(os.path.exists('E:\\kod\\Automate_the_boring_stuff\\chap11a.py'))
print(os.path.exists('E:\\kod\\Automate_the_boring_stuff\\ugabugfaaaaa.py'))
print('')

# check if file, or if folder
print(os.path.isfile('E:\\kod\\Automate_the_boring_stuff\\chap11a.py'))
print(os.path.isfile('E:\\kod\\Automate_the_boring_stuff'))
print(os.path.isdir('E:\\kod\\Automate_the_boring_stuff\\chap11a.py'))
print(os.path.isdir('E:\\kod\\Automate_the_boring_stuff'))

# size of path in bites
print(os.path.getsize('E:\\kod\\Automate_the_boring_stuff\\chap11a.py'))
# returns list of strings of files and folders insdide that folder. 
print(os.listdir('E:\\kod\\Automate_the_boring_stuff'))


# print size of all files in a folder
totalSize = 0
for filename in os.listdir('E:\\kod\\Automate_the_boring_stuff'):
    if not os.path.isfile(os.path.join('E:\\kod\\Automate_the_boring_stuff', filename)):
        continue
    # if is file, add its size. 
    totalSize = totalSize + os.path.getsize(os.path.join('E:\\kod\\Automate_the_boring_stuff', filename))

print(totalSize)


#create directories! either absolute or relative path.!!!!

#os.makedirs('E:\\kod\\Automate_the_boring_stuff\\folder1\\folder2\\folder3')
#os.makedirs('relativePath')





