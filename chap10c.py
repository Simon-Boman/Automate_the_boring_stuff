import re
#may want to match a number of repetitions of our group!

#? optional group, says match the group zero or once

#? says this group (wo) can appear zero or once in order to match this pattern
batRegex = re.compile(r'Bat(wo)?man')
# will match Batman
mo = batRegex.search('The Adventures of Batman')
print(mo.group())
# will also match Batwoman, cause the wo-group can appear 1 or 0 times.
# above appears 0 times, but here it appears once. 
mo = batRegex.search('The Adventures of Batwoman')
print(mo.group())
# this wont match, cause the wo-group can only appear 0 or 1 times
mo = batRegex.search('The Adventures of Batwowowoman')
print(mo==None)
print('')

#can make phonenumber regex that looks for optional area code.
# this is the default once that requires full area code
phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneRegex.search('My phone number is 415-555-1234. Call me!')
print(mo.group())
#so add group, and ?, so this group can appear onceo or zero times. 
#now returns match for both these cases. 
phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo = phoneRegex.search('My phone number is 415-555-1234. Call me!')
print(mo.group())
mo = phoneRegex.search('My phone number is 555-1234. Call me!')
print(mo.group())
print('')

#if need to match literal ?, add \?
#. e.g. if looking for "dinner?", then we could do
# re.compile( r'dinner\?' )

# * - star, match 0 or more times
batRegex = re.compile(r'Bat(wo)*man')
mo = batRegex.search('The Adventures of Batman')
print(mo.group())
mo = batRegex.search('The Adventures of Batwoman')
print(mo.group())
mo = batRegex.search('The Adventures of Batwowowowoman')
print(mo.group())
print('')
#if need to match literal *, add \*

# + plus, match 1 or more times. must appear at least once
batRegex = re.compile(r'Bat(wo)+man')
#thus this wont find match, cause doesnt have wo
mo = batRegex.search('The Adventures of Batman')
#but these will match, cause wo-group appears at least once
mo = batRegex.search('The Adventures of Batwoman')
print(mo.group())
mo = batRegex.search('The Adventures of Batwowowowoman')
print(mo.group())
print('')
#if need to match literal +, add \+

#escaping ?, *, +
regex = re.compile(r'\+\*\?')
mo = regex.search('I learned about +*? regex syntax')
print(mo.group())
#group must appear one or more times
regex = re.compile(r'(\+\*\?)+')
mo = regex.search('I learned about +*?+*?+*?+*? regex syntax')
print(mo.group())
print('')

# if want to match exact number of times, {x}
haRegex = re.compile(r'(Ha){3}')
mo = haRegex.search('He said "HaHaHa"')
print(mo.group())
#optional area code, put all in group, match 3 numbers in a row with optional comma
phoneRegex = re.compile(r'((\d\d\d-)?\d\d\d-\d\d\d\d(,)?){3}')
mo = phoneRegex.search('My numbers are 415-555-1234,555-4242,212-555-0000')
print(mo.group())
print('')

# match range number of times, {3,5}, min,max
# {,5} same as 0-5 ; {3, } same as 3-infinity
haRegex = re.compile(r'(Ha){3,5}')
mo = haRegex.search('He said "HaHaHa"')
print(mo.group())
mo = haRegex.search('He said "HaHaHaHaHa"')
print(mo.group())
mo = haRegex.search('He said "HaHaHaHaHaHaHaHaHaHa"')
print(mo.group()) # still matches, but only to max limit of 5 Ha
print('')


digitRegex = re.compile(r'(\d){3,5}')
mo = digitRegex.search('1234567890')
print(mo.group()) #returns the first, 5 characters it matches with
# i.e. 12345. also matches with maximum number of characters i.e. longest string
# could also match with 67890, or 123, or 2345...
# so first occurence, and longest possible - GREEDY matching!

#can specify non-greedy match with ? after {3,5}. 
# different from the ? that means 0 or 1.
# when it comes after a pattern like this, it means do a NON-GREEDY match
#so matches first SHORTEST possible string
digitRegex = re.compile(r'(\d){3,5}?')
mo = digitRegex.search('1234567890')
print(mo.group())