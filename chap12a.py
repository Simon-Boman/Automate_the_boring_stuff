# previously we used try and except statements
# can also raise your own exceptions - i.e. stop running and move execution to exception.

# if no try and except statements handling the exception, program simply crashes and displlays the Exception message.
#raise Exception('This is the error message.')

"""

******************
*                *
*                *
*                *
******************

"""

def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('"symbol" needs to be a string of length 1.')
    if (width < 2) or (height <2):
        raise Exception('"width" and "height" must be greater or equal to 2.')
    print(symbol * width)

    for i in range(height - 2):
        print(symbol + (' ' * (width-2)) + symbol)

    print(symbol * width)

boxPrint('*', 15, 5)
boxPrint('O', 5, 16)

#boxPrint('**', 15, 5) #causes bug, not working the way we intended it to work
#boxPrint('*', 1, 1) #also doesnt work as intended. 
# the exceptions generate a traceback/call stack, so you can track the error. 
# can get this text as a string value:
print('')

import traceback
try:
    raise Exception('This is the error message for TRACEBACK EXAMPLE!')
except:
    errorFile = open('error_log.txt', 'a')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('The traceback info was written to error_log.txt')
    print('')


# assertions and the assert statements 
# sanity check that code does what it should
# if assert <code>==False , raises assert exception
#assert 1 == 5, 'This is the error message for ASSERTION!'

secondStreet = {'ns': 'green', 'ew': 'red'}

def switchLights(intersection):
    for key in intersection.keys():
        if intersection[key] == 'green':
            intersection[key] ='yellow'
        elif intersection[key] == 'yellow':
            intersection[key] ='red'
        elif intersection[key] == 'red':
            intersection[key] ='green'
    #if no light is red, print this out! shouldnt happen. traffic going in both directions. 
    assert 'red' in intersection.values(), 'Neither light is red!' + str(intersection)
print(secondStreet)
switchLights(secondStreet)
print(secondStreet)

#unlike try except, when an assert fails the code should crash, cause they are sanity checks that shouldnt happen. 
#asertion is for PROGRAMMING errors, not USER errors. 
#errors that can be recovered from, e.g. file not found, wrong input - raise exception instead, so can recover from it! ! 