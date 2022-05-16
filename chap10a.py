import re #module with regular expression

#create regex objeect
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') #give compile the pattern (raw string, so can track \ also),
#and store the regular expression object. 
# \d says we are looking for a digit

# the regular expression data type (i.e. any regular expression object, like phneNumRegex which we got from using compile(pattern)),
# has a search method, which can be used to search a string for the pattern. 
# this returns a match object (mo). 
mo = phoneNumRegex.search( 'Call me at 415-555-1011 tomorrow, or at 415-555-9999 to my office.')

# match objects have a method called group, which will give you the actual matching text
print(mo.group())

#findall-method gives us all occurences, not just first. 
mo = phoneNumRegex.findall( 'Call me at 415-555-1011 tomorrow, or at 415-555-9999 to my office.')
print(mo)