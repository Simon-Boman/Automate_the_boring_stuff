#Can do many things with a string that you can do with a list! 
print(list('Hello'))

name = 'Simon'
print(name[0])
print(name[1:3])
print(name[-1])
print('mon' in name)

for letter in name:
    print(letter)
print('')

#List is MUTABLE - can have values added, removed, changed
#Strings are IMMUTABLE - can not add, remove, or change from string. So must create new.
name = 'Simon a boss'
newName = name[:5] + ' the ' + name[8:]
print(newName)
print('')


#cheese just copies value of spam - does NOT reference to spam, so will not get affected by the reassignment of spam. 
spam = 42
cheese = spam
spam = 100 #cheese DOES NOT GET MODIFIED IF WE MODIFY spam
print(spam)
print(cheese)

#for lists, they use REFERENCES! So can have 2 references to the SAME list! 
#all MUTABLE data types use REFERENCES. the variable doesnt contain the values, just the reference (to memory)
spam = [0, 1, 2, 3, 4, 5]
cheese = spam
cheese[1] = 'Hello!'
print(cheese)
print(spam) #spam ALSO GETS MODIFED IF WE MODIFY cheese 
print('')

#The reference here, cheese, refers to the SAME LIST as the global SPAM!
#So even tho cheese variable gets destroyed, the changes in spam are reflected otuside of the function! 
def eggs(cheese) :
    cheese.append('Hello')

spam = [0, 1, 2, 3, 4, 5]
eggs(spam)
print(spam)
print('')

import copy
#can make DEEP COPY of a list, i.e. not just copy reference, but create a brand new list with the same values.
cheese = copy.deepcopy(spam)
cheese.append("hehe only affects cheese")
print(cheese)
print(spam)
print('')

