import pyperclip
import re

# Create a regex for phone numbers
phoneRegex = re.compile(r'''
# 415-555-0000, 555-0000, (415) 555-0000, 555-0000 ext 12345, ext. 12345, x12345
(
((\d\d\d)|(\(\d\d\d\)))?    # area code (optional) - group 1 - 415 ; group 2 - (415). group 3 - add ? to (0 or 1) the whole thing, since the whole area code is optional.  
(\s|-)    # first separator
\d\d\d    # first 3 digits
-    # separator
\d\d\d\d  # last 4 digits
(((ext(\.)?\s)|x)        # extension word-part (optional) - ext, add group with . and ? for ext., since the dot is optional. | we can just have an x. 
(\d{2,5}))?    # extension number-part (optional) - followed by a group of 2-5 digits. finally, add group around everyrhing with ?, so entire group is optional. 
) #put everything into large group 0 - so we can cover the entire matched text for printing out
''', re.VERBOSE)


# Create a regex for email addresses
emailRegex = re.compile(r'''
# something@something.com ; some.thing@ ; some+thing@ ; some_thing@ ; @some.thing.com @some+thing.com @some_thing.com 

[a-zA-Z0-9_.+]+    # name part - create character class! this can be in the name part. + - search for 1 or more of them (needs 1... not optional) 
@    # @ symbol
[a-zA-Z0-9_.+]+    # domain name part
''', re.VERBOSE)


# Get the text off the clipboard
copiedText = pyperclip.paste()

# Extract the email/phone from this text
#our regex has 2+ groups, so returns list of tuples for each match, and each tuple has several strings in it, one string for each of the groups
#so, we put the whole phoneregex in one large group 0. 
extractedPhone = phoneRegex.findall(copiedText) 

#save just group 0 with full number
allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

# Copy the extracted email/phone to the clipboard
extractedEmail = emailRegex.findall(copiedText) #no groups, so returns a list of strings

results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)  #put allPhoneNubmers and emails into a string, join on \n, i.e. new line for each
#print(allPhoneNumbers)
#print(extractedEmail)
print(results)
pyperclip.copy(results) #copy result to clipboard. 
