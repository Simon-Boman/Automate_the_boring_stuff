print('Hello World!') #call to the print function, passing string Hello World as argument
print('What is your name?') 
myName = input() #input to the input function evaluate to a string (of what we input)
print('It is good to meet you, ' + myName)
print('The length of you name is: ' + str(len(myName)))

print('What is your age?')
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year.')