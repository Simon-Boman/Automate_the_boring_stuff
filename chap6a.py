spam = ['a', 'b', 'c', 'd', 'e', 'f']

print(spam[-1])
print(spam[-6])
print('')

print(spam[1:3])
print(spam[1:3][0])
print('')

spam[0] = 'aa'
print(spam[0])
spam[1:3] = ['bb', 'cc', 'bbccxD', 'replaced 2 but added 4!']
print(spam)
print('')

#slicing shortcuts:
#leave out first index: same as using 0
#leave out last index: same as using END index
spam = ['a', 'b', 'c', 'd', 'e', 'f']
print(spam[:2])
print(spam[2:])
print('')

#delete from list
del spam[0]
print(spam)
print('')

#len, concatination, and replication work the same with lists as with strings
print(len(spam))
concat = [1,2,3] + [5,6,7]
print(concat)
concat2 = concat * 3
print(concat2)
print('')

#can convert string to list using list()
print(list('Converted to list'))
print('')

#using in, and not in
print(5 in concat)
print(55 in concat)
print(5 not in concat)

