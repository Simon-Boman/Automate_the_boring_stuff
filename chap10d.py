import re

phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
#findall finds ALL matches of the regex pattern with findall(). Returns a list of strings
# find all does not return a match object like search does! just lists
resume = ''' erugn rigjreog orejigerui ergjnreg 508-555-5555, jrneger
ergjnerg ergjknergg 234-234-2343 jergni 322-222-2222.
gregjkg ergeklrg.
'''
print(phoneRegex.findall(resume))
# if the regex has 0 or one () group, then the findall returns a list of string,
# and each entry in the list of its exact match. 

# if 2 or more groups, instead returns list of tuples of strings,
# where each tuple is the match in the text, and consist of the
# groups matches! 
phoneRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
print(phoneRegex.findall(resume))

#above, we dont include the "-" cause there is no group that matches that.
# so if we want the entire string aswell, put everything in its own group.
phoneRegex = re.compile(r'((\d\d\d)-(\d\d\d-\d\d\d\d))')
print(phoneRegex.findall(resume))


#character class - e.g. \d - any numeric digit
#digitRegex = re.compile(r'\d'), better than re.compile(r'(0|1|2|3|4|5|6|7|8|9|0')
#\d digit - \D - character that is NOT numeric digit, \w - any word character (letter, digit, underscore)
# \D anything that is NOT a letter, numerici digit, or underscore
# \s for space characters (space, tab, newline). \S - anything that is NOT space characters

lyrics = '''12 drummers drumming,
11 pipers piping,
10 lords a-leaping,
9 ladies dancing,
8 maids a-milking,
7 swans a-swimming,
6 geese a-laying,
5 golden rings,
4 calling birds,
3 French hens,
2 turtle doves
1 a partridge in a pear tree.'''

#find number followed by some characters
# \d+ - one or more digits, covers both cases of 1 or 2 digits
# \s space
# \w word characters, letters, numbers, 1 or more. 
xmasRegex = re.compile(r'\d+\s\w+')
print(xmasRegex.findall(lyrics))


#can make your own character classes 
# add all characters we want to be in our character class in []
vowelRegex = re.compile(r'[aeiouAEIOU]') #better than r'(a|e|i|o|u|A...)'
vowelRegex2 = re.compile(r'[a-fA-F]') #can do like this to get range
print(vowelRegex.findall('Robocop eats baby food.'))

#match 2 vowels in a row
doubleVowelRegex = re.compile(r'[aeiouAEIOU]{2}')
print(doubleVowelRegex.findall('Robocop eats baby food.'))

#negative character class - add ^
# will match any character that is NOT in this!
# so basically we find all consonants (and spaces, dots..)
consonantsRegex = re.compile(r'[^aeiouAEIOU]')
print(consonantsRegex.findall('Robocop eats baby food.'))