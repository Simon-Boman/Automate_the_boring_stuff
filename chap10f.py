import re

#search, findall is like ctrl+f search...
#but we can also do FIND AND REPLACE! 

namesRegex = re.compile(r'Agent \w+') #Agent + 1 or more word characters. Stops at space. 
print(namesRegex.findall('Agent Alice gave the secret documents to Agent Bob.'))

#sub (substitute)-method, finds and replaces!
print(namesRegex.sub('REDACTED', 'Agent Alice gave the secret Documents to Agent Bob.'))
print('')

#can use parts of the original match! to do this use \number, the numbers stand for the GROUPS in the original regex. 
namesRegex = re.compile(r'Agent (\w)\w*') #Agent + 1 character word in group + 0 or more characters
print(namesRegex.findall('Agent Alice gave the secret documents to Agent Bob.')) #now, doesnt return the entire match, just the GROUP! 
print(namesRegex.sub(r'Agent \1****', 'Agent Alice gave the secret Documents to Agent Bob.')) #\1 means use text from group 1 of the match for the substituted text!


#Verbose regex format! 
re.compile(r'(\d\d\d)(-)?\d\d\d-\d\d\d\d') #these expressions get really out of hand...

#so, use Verbose format!!!
re.compile(r'''
\d\d\d  #area code
-       #first dash
\d\d\d  #first 3 digits
-       #second dash
\d\d\d\d #last 4 digits''', re.VERBOSE) #verbose mode - whitespace in string doesnt match the actual pattern we want to match! So can add ''' and use more lines! 

re.compile(r'''
(\d\d\d-)|  #area code (without parens, with dash)
(\(\d\d\d\) ) #-or- area code with parens and no dash
\d\d\d  #first 3 digits
-       #second dash
\d\d\d\d #last 4 digits
\sx\d{2,4} #extension, like x1234 ''', re.VERBOSE) #verbose mode - whitespace in string doesnt match the actual pattern we want to match! So can add ''' and use more lines! 



#to combine settings to compile, can do: re.compile(...., re.IGNORECASE | re.DOTALL | re.VERBOSE) 