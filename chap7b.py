import pprint

cat = {'name': 'Simon', 'age': 7, 'color': 'gray'}

allCats = []
allCats.append(cat)
allCats.append({'name': 'Boman', 'age': 71, 'color': 'brown'})
allCats.append({'name': 'Brolle', 'age': 5, 'color': 'yellow'})
allCats.append({'name': '???', 'age': -1, 'color': 'white'})
print(allCats) #this list of dictionaries is a type of data structure. model real world things, that our program can understand. 
print('')

#e.g. tic-tac-toe board
theBoard = {'top-L': 'O', 'top-M': 'X', 'top-R': 'X', 'mid-L': 'X', 'mid-M': 'O', 'mid-R': ' ', 'low-L': 'X', 'low-M': ' ', 'low-R': 'O'}
pprint.pprint(theBoard)

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-----')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-----')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
    print('-----')
    
printBoard(theBoard)
print('')


print(type(42))
print(type(3.14))
print(type('Hello'))
print(type(theBoard)) #dict
print(type(theBoard['top-R'])) #string
print(type(allCats))
print('')


#nestled dictionaries and lists
#here we have a dictionary, where the value is also a dictionary. 
allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
             'Bob': {'ham sandwiches': 3, 'apples': 2},
             'Carol': {'cups': 3, 'apple pies': 1}}
print(allGuests)
print(allGuests.get('Alice', ' '))

def totalBrought(guests, item):
    numBrought = 0
    for k, v in guests.items(): #k = key, v = value of each entry in guests. k is name ( 'Alice' ), v is dict of foods ( {'apples': 5, 'pretzels': 12} )
        numBrought = numBrought + v.get(item, 0)
    return numBrought

print('Number of things being brought:')
print(' - Apples         ' + str(totalBrought(allGuests, 'apples')))
print(' - Cups           ' + str(totalBrought(allGuests, 'cups')))
print(' - Cakes          ' + str(totalBrought(allGuests, 'cakes')))
print(' - Ham Sandwiches ' + str(totalBrought(allGuests, 'ham sandwiches')))
print(' - Apple Pies     ' + str(totalBrought(allGuests, 'apple pies')))
