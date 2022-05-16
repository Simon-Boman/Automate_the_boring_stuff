
#TUPLES ARE LIKE LISTS . BUT IMMUTABLE! USE E.G. IF DONT INTEND TO CHANGE ITS CONTENTS! 
eggs = ('hello', 42, 0.5)
print(eggs[0])
print(eggs[1:3])
print(len(eggs))

#eggs[1] = 99 #ERROR

print(type( ('hello',) ))
print(type( ('hello') ))
print('')

#can CONVERT LIST TO TUPLE, AND TUPLE TO LIST!
print( tuple( ['cat', 'dog', 5] ) )
print( list( ('cat', 'dog', 5) ) )
print(list('hello'))