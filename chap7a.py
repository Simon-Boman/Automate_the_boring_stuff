#dictionaries are unordered, compared to lists which are ordered. 
#dictionaries are mutable like lists. the variable holds a reference to the dictionary, not the dictionary itself. 
print([1,2,3] == [3,2,1]) 
eggs = {'name': 'Simon', 'age': 24}
ham = {'age': 24, 'name': 'Simon'}
print(eggs == ham)
print('')

#key-value pairs in braces
myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
print('My cat has ' + myCat['color'] + ' fur.')
#can us ints for keys
spam = {12345: 'Luggage combination', 42: 'The Answer'}
print(spam[12345])
print('')

print('size' in myCat) #can use in and not in for dictionaries also. 
print('size' not in myCat)
print('fat' in myCat.values()) #can also check for values
print('')

print(myCat.keys()) #returns keys 
print(myCat.values()) #returns values
print(myCat.items()) #returns 2-item tuples of key, value. So here we get three tuples with key,value. tuples like lists but immutable!
keys = list(myCat.keys()) # these all return list-like datatypes. can transform to list. 
print(keys) 
print('')

for key in myCat.keys():
    print(key)
for val in myCat.keys():
    print(val)
for key, val in myCat.items(): #multipele assignment trick
    print(key, val)
for i in myCat.items():
    print(i)
print('')


##USE GET INSTEAD OF DICT['']
#get - second argument, fallback value if that key doesnt exist in the dictionary. 
print(myCat.get('size'), '')
print(myCat.get('color'), '')
print(myCat.get('kids'), '')
picnicItems = {'apples': 5, 'cups': 2}
print('I am bringing ' +  str(picnicItems.get('napkins', 0)) + ' to the picnic.')

#setdefault - set value ONLY IF KEY DOESNT EXIST. 
myCat.setdefault('color', 'black') #doesnt set, since color key already exists
myCat.setdefault('kids', 5) #sets kids to be 5, since kids key does not exist
print(myCat)