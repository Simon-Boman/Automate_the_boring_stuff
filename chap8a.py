#if we want quote in a string
print("That is Simon's cat.")

#escape characters, single/double quote, tab, newline, backslash!
print('That is Simon\'s cat.')
print('Hello there!\nHow are you?\nI\'m fine.')
print('')

#raw strings - if text with many backslashes THYAT WE DONT WANT TO SEE AS ESCAPE CHARACTERS,
# e.g. windows path, or regex pattens, can be useful to use raw strings! 
rawString = r'That is Simon\'s cat.'
print(rawString)
print('')

#multiline strings - ''' or """
print("""Hello,
This is a multiline string!
Dont need to use escape characters.""")
print('')

#A string is a list-like value, with each character being a value in that list.
spam = 'Hello World!'
print(spam[0])
print(spam[1:5])
print(spam[-1])
print('Hello' in spam)
