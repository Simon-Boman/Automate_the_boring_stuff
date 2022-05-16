def div42by_noob(divideBy):
    return 42 / divideBy

# crashes and terminates the program when error occurs
print(div42by_noob(5)) 
# if we try to print this, will crash
#print(div42by_noob(0)) 
print(div42by_noob(1), '\n') 


def div42by_specifiedExcept(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: You tried to divide by zero!')

print(div42by_specifiedExcept(5)) 
print(div42by_specifiedExcept(0)) # in try clause, if causes the ZeroDivisionError except, execution moves to the code in except clause. The function returns None, and thus we print None. 
print(div42by_specifiedExcept(1), '\n') 



#can simply put except and nothing else. useful for input validation. 
def div42by(divideBy):
    try:
        return 42 / divideBy
    except:
        print('Error: You tried to divide by zero!')

print(div42by(5))
print(div42by(0))
print(div42by(1), '')

print('\nHow many cats do you have?')
numCats = input()
try: 
    if int(numCats) >= 4:
        print('That is a lot of cats.')
    else:
        print('That is not that many cats')
except ValueError:
    print('You did not enter a number.')
#if input "six", causes crash, cause we expect numerical value, not string. so add try and except. 