#string methods return a new string rather than modify the string in place, since strings are IMMUTABLE
hello = 'hElLo xD'
print(hello.upper())
print(hello.lower())
#however this does not change the hello variable, then we would need to e.g.
helloUpper = hello.upper()
print(helloUpper)
print('')

#islower(), isupper()
hello = "HELLO"
print(hello.islower())
print(hello.isupper())
print('1234'.islower()) #since no letters, returns true
print('1234'.isupper())
print('Hello'.upper().isupper()) #returns true, since convert to upper, then check if upper
print('')

print('Hello'.isalpha())
print('password12345'.isalnum())
print('123'.isdecimal())
print('     '.isspace())
print('True, If All Words Inside Starts With Uppercase, Then Lowercase'.istitle())
print('convert to title!'.title())
print('')

print('Hello world!'.startswith('Hello'))
print('Hello world!'.startswith('H'))
print('Hello world!'.endswith('world!'))
print('Hello world!'.endswith('world'))
print('')

#join - join string with a list of strings, into a new string
print( ',\n'.join(['cats', 'rats', 'bats']) )

#split - splits string, and returns a list of strings
print('My name is Simon'.split()) #splits on whitespace by default
print('My name is Simon'.split('m'))
print('')

#adds padding by adding spaces to the left/right/center. parameter is the length we want the total string to be. 
print('Hello'.rjust(10) + '.')
print('Hello'.ljust(10) + '.')
print('Hello'.rjust(20, '*')) #can specify other fill character
print('Hello'.center(20, '='))
print('')

#strip if whitespace characters, spaces, tabs, newlines, to the left/right or both sides.
spam = 'Hello'.center(20)
print(spam.strip()) #remove whitespaces from both sides
spam = 'Hello'.center(20, '=')
print(spam.rstrip('=')) #remove whitespaces from right side
spam = "SpamSpamBaconSpamEggsSpamSpam"
print(spam.strip('maSp')) #order doesnt matter, just specify letters. 
#NOTE: still spam in middle. Because removes those letters UP TO FIRST and DOWN TOT LAST letters which does not contain anything we try to strip. 
print('')

#replace() - replaces a substring with another substring everywhere in the string
spam = 'Hello there!'
print(spam.replace('e', 'XYZ'))

import pyperclip

pyperclip.copy('Hellooooooo!!!!!!!!!') #paste this to clipboard
print(pyperclip.paste()) #return what is copied in clipboard