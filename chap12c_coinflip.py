import random

heads = 0

for i in range(1, 1001):
    if random.randint(0, 1) == 1:
        heads = heads + 1
    if i == 500:
        print('Halfway done!') # e.g. add breakpoint here, will doo 500 iterations and reach here,
        #and we can see e.g. value of heads and i here! 

print('Heads came up ' + str(heads) + ' times.')