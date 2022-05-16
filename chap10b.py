import re
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 415-555-4242')
print(mo.group())
print('')

#if we just want the area code, or just the phone number part, 
#can use paranthesis to mark out GROUPS in the phoneNumRegex. 
#NOTE! the paranthesis does not mean that we want to MATCH on them
import re
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242')
print(mo.group())
print(mo.group(1)) #we now also have 2 individual groups!
print(mo.group(2))
print('')

#if you want to find literal paranthesis,
#e.g. (415) 555-4242 is number, then we wanna find literal parantehsis.
#then use (

phoneNumRegex = re.compile(r'(\d\d\d) \d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is (415) 555-4242')
print(mo.group())
print('')

# | - pipe character. can use pipe to match one of several patterns
# as part of your regex. E.g. match batman, batmobile, or batcopter
# add Bat(and suffixesseparated with | )
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group())
#if we want to find out which suffix was found, we can just pass
#1 to the group method.
print(mo.group(1))

mo = batRegex.search('Batmotorcycle lost a wheel') #returns NONE
#print(mo.group()) #so cant print, since cant all group on None.