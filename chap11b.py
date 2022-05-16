# plaintext files, .txt - just text. 
# binary files - all other files, word procesing files, images, executable files, etc. 

# read mode - can only read. Returns file object
helloFile = open('E:\\kod\\Automate_the_boring_stuff\\hello.txt')

# file object has methods, e.g. read() - returns string
contents = helloFile.read()
print(contents)

# close file after
helloFile.close()

# can also do readlines - returns lines as strings in a list
helloFile = open('E:\\kod\\Automate_the_boring_stuff\\hello.txt')
contents = helloFile.readlines()
print(contents)
helloFile.close()
print('')

# can open file in write/append mode. write mode - will overwrite the file. append mode - will append text to end of file. 
# specify by adding , 'w' or 'a'
# if file doesnt exist, python will create new. 
helloFile = open('E:\\kod\\Automate_the_boring_stuff\\hello2.txt', 'w')

# write() to e.g. pass string
helloFile.write('Hello!!!!!!!\n')
helloFile.write('Hello!!!!!!!')
helloFile.close()

#can also use relative file paths, and will look for/create in current working directory. 
baconFile = open('bacon.txt', 'w')
baconFile.write('Bacon is not a vegetable.')
baconFile.close()

baconFile = open('bacon.txt', 'a')
baconFile.write('\n\nBacon is delicious.')
baconFile.close()


# the shelve mode - if you wanna store variables that have list, or dictionaries, or nontext data.
# can then save variables as binary shelf files. 
import shelve
shelfFile = shelve.open('mydata') #opens shelv file object
# can make changes to shelf value as if it was a dictionary. then just call close.
shelfFile['cats'] = ['Simon', 'Gustav', 'Kattis', 'Fatty', 'Catty']
shelfFile.close()

#can now grab values like a dictionary! 
shelfFile = shelve.open('mydata')
print(shelfFile['cats'])

#shelf files very similar to lists. can do .keys() and .values()
print(list(shelfFile.keys()))
print(list(shelfFile.values()))
