a = '42'
b = 42
c = 42.0
print(b!=c)
print('')

print('What is your name?')
#name=input()
name = 'simon'
if name:
    print("hello "  + name)
else:
    print("No name was given")
print('')


#see if truthy or falsy
print(bool(0))
print(bool(1))
print('')


i = 0
while i < 5:
    print('Hello world')
    i += 1
print('')


name = ''
while name != 'Simon':
    print('Please type "Simon"')
    name = input()
print('Thank you!')
print('')

#using break - leaves loop, without rechecking the loop condition. 
name = ''
while True:
    print('Please type "Simon"')
    name = input()
    if name == 'Simon':
        break
print('Thank you!')
print('')


#continue - jumps back to the start of the loop and rechecks the loops condition
spam = 0
while spam < 5:
    spam += 1
    if spam == 3:
        continue
    print('span is: ' + str(spam))
print('')


for i in range(5):
    print(i)
print('')

i = 0
while i < 5:
    print(i)
    i += 1
print('')

for i in range(12, 16): #start, stop
    print(i)
print('')


for i in range(0, 10, 2): #start, stop, increment
    print(i)
print('')

for i in range (5, -1, -1):
    print(i)
print('')



