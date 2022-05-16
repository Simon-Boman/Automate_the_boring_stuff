def hello():
    print('Hello!')
    print('Hello!!!')
    print('Hello there!!!!!!\n')

def helloName(name):
    print('Hello ' + name + '\n')

def plusOne(number):
    return number+1

hello()

helloName('Simon')

print(plusOne(5))



#None - lack of value (null)

spam = print() #print actualyl returns None (null). If function doesnt have return value, then it returns None. 
print(spam)
print(spam == None)
print('')


#keyword arguments (optional), "end", "sep"
print('Hello', end = '') #end, usually adds newline. we can change it, so it does not add anything (or adds something we define)
print('World')

print('cat', 'dog', 'mouse', sep='xD') #by default, adds space, if we specify "sep", can change waht separating cahracter is. 