name = 'Simon'
place = 'Linkan'
time = '16:04'
food = 'pizza'
bigString = 'Hello ' + name + ', you are invited to a party at ' + place + ' at ' + time + '. Please bring ' + food + '.'
print(bigString)  

#string FORMATTING / string interpolation.
#put a %s inside a string to mark where we wanna have other strings inserted into it. 
#followed by a % and a () comma separated list of values to insert at the %s. the %s are called CONVERSION SPECIFIERS. 
bigString2 = 'Hello %s, you are invited to a party at %s at %s. Please bring %s. ' % (name, place, time, food)
print(bigString2)