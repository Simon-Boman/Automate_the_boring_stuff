import re

#match at ^BEGGINING end ENDING$ of string
beingsWithHelloRegex = re.compile(r'^Hello') #the text pattern must begin at the beginning of the string
print(beingsWithHelloRegex.search('Hello there'))
print(beingsWithHelloRegex.search('He said Hello!'))
print('')
endsWithWorldRegex = re.compile(r'world!$')
print(endsWithWorldRegex.search('Hello world!'))
print(endsWithWorldRegex.search('Hello world!regrgregeg'))
print('')

#^both$ means pattern must match the entire string
allDigitsRegex = re.compile(r'^\d+$') #start with digit, end with digit. + to indicate 1 or more! 
print(allDigitsRegex.search('123234324325353543535')) 
print(allDigitsRegex.search('1232x343243x25353543535')) 
print('')


# . wildcat - ANY CHARACTER except for the newline!
atRegex = re.compile(r'.at') #matches with the string <any character> + at
print(atRegex.findall('The cat in the hat sat on the flat mat.'))
atRegex = re.compile(r'.{1,2}at') #matches with the string <1 or 2 of any character> + at, these characters can be spaces! 
print(atRegex.findall('The cat in the hat sat on the flat mat.'))
print('')


# .* to match anything. . -any character,* = 0 or more. 
nameRegex = re.compile(r'First name: (.*) Last name: (.*)')
print(nameRegex.findall('First name: Simon Last name: Boman')) #for find all, this regex contains groups, so will return a list of tuples of strings 

# .* uses greedy matchning, i.e matches as much as possible. Use .*? for non greedy, i.e. match with as little as possible. 
serve = '<To serve humans> for dinner.>'
nonGreedyRegex = re.compile(r'<(.*?)>')
print(nonGreedyRegex.findall(serve))
greedyRegex = re.compile(r'<(.*)>')
print(greedyRegex.findall(serve))
print('')


prime = 'Serve the public trust. \nProtect the innocent.\nUphold the law. '
print(prime)
 
dotStar = re.compile(r'.*')
print(dotStar.search(prime)) #will match UNTIL IT REACHES NEWLINE, since . can be any character EXCEPT newline \n

#but we can get the . to mean actually everything by passing re.DOTALL
dotStarAll = re.compile(r'.*', re.DOTALL)
print(dotStarAll.search(prime))
print('')


# case insensitive regex match. - re.IGNORECASE
voewlRegex = re.compile(r'[aeiou]', re.IGNORECASE)
print(voewlRegex.findall('Al, why does your programming book talk about RoboCop so much?')) #now also matche with capital voewls! 

