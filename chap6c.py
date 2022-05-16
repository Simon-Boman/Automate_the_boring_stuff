spam = ['hello', 'hi', 'howdy', 'heyas', 'hello']
print(spam.index('hi')) # index is a list METHOD - must be called on an object with .METHOD()
print(spam.index('hello')) #if multiple exists, will return first
print('')

spam.append('SIEMA') #append adds to END
print(spam)
spam.insert(1, "YAHOO") #insert adds to THE INDEX and everything else is bumped up 1 index
print(spam)
spam.remove('hello') #REMOVE removes from list, if multiple exists removes first 
print(spam)
print('')

ints = [2, 5, 3.14, 1, -7]
ints.sort()
print(ints)
strings = ['ants', 'cats', 'dogs', 'badgers']
strings.sort()  
print(strings)
strings.sort(reverse=True) #SORT IN REVERSE ORDER
print(strings) 
# ASCII-order for sorting strings, i.e. capital letters come before lower case. 
strings = ['Alice', 'Bob', 'ants', 'cats', 'dogs', 'Carol', 'badgers']
strings.sort()  
print(strings)
strings.sort(key=str.lower) #SORT ON TRUE ORDER: basically passes on the convert to lower case method
print(strings)