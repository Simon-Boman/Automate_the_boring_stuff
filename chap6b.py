for i in [0, 1, 2, 3]: #same as using range(4)
    print(i)
print('')

#range function returns range object. its a list-like value, but technically named sequence.
print(range(4)) #essentially the same as a list object [0, 1, 2, 3]
actualList = list(range(4))
print(actualList)
print('')

#can use this to get collection of integers in a list:
print(list(range(0, 100, 2)))
print('')

# for i in RANGE(LEN(LIST)) - very nice when need both list items and index of it
supplies = ['pens', 'staplers', 'flamethrowers', 'bimders']
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' +supplies[i])
#ENUMERATE does exactly the same as above! 
for index, item in enumerate(supplies):
    print('Index ' + str(index) + ' in supplies is: ' + item)
print('')

#multiple assignments on one row! 
cat = ['fat', 'orange', 'loud']
size, color, disposition = cat # if 3 variables, 3 items in list, can do this
print(size, color, disposition)
size, color, disposition = 'skinny', 'black', 'quit'
print(size, color, disposition)

a = 'AAA'
b = 'BBB'
a, b = b, a
print(a,b)
print('')

#Augmented assignment operator
spam = 42
spam += 1
print(spam)
