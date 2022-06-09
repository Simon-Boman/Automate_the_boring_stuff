# logging module - can use log messages to find bugs
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# logging to a file instead: change config to filename='chap12bLog.txt'
# logging.basicConfig(filename='chap12bLog.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# 5 levels of logging - debug(lowest), info, warning, error, critical(highest)
# logging.debug() creates logging at debug-level, etc... 
# so, e.g. logging.disable(logging.CRITICAL) disables loggings at critical OR lower level. 

# can now use logging.debug()-calls, like print calls but some more information. 
# if we use logging.debug instead of print, we can just delete all logging.debug prints (whereas we could want to keep some prints)
# AND, we can just at the top call logging.disable(logging.CRITICAL) - disables all log messages
# logging.disable(logging.CRITICAL)
# logging.disable(logging.INFO)

logging.debug('Start of program')

def factorial(n):
    logging.info('Start of factorial (%s)' % (n))
    total = 1
    for i in range(n + 1):
        total *= i
        logging.warning('i is %s, total is %s' % (i, total))
    logging.info('Return value is %s' % (total))
    return total

print(factorial(5))

logging.debug('End of program')

# easy to find bug, that we start at i = 0, so we get total = 1*0 = 0

print()
def factorialFixed(n):
    total = 1
    for i in range(1, n + 1):
        total *= i
    return total
print(factorialFixed(5))

