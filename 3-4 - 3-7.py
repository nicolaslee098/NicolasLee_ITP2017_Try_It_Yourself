print ('Names of guest: ')
names = ['pier', 'dumac', 'excel']
print (names)
print ('Guest who can not come: ')
print (names[2])
del names [2]
print ('New guest: ')
print ('las')
print ('Names of guest: ')
names.append ('las')
print (names)
print ('more guest: ')
names.insert(3, "alex")
names.insert(4,'xela')
names.append ('jojo')
print (names[3], names[4], names [5])
print ('Guest: ')
print (names)
print ('names of guest who will attend the party after removing some: ')
names.pop(0)
names.pop(1)
names.pop(2)
names.pop()
print (names)
names = ('pier', 'dumac', 'las', 'alex', 'xela', 'jojo')
message = ('dear ' + names[0] + ', i am sorry to inform you that you had been removed from the dinner party due to a restaurant table issue, hope you still love me.')
print (message)
message = ('dear ' + names[2] + ', i am sorry to inform you that you had been removed from the dinner party due to a restaurant table issue, hope you still love me.')
print (message)
message = ('dear ' + names[4] + ', i am sorry to inform you that you had been removed from the dinner party due to a restaurant table issue, hope you still love me.')
print (message)
message = ('dear ' + names[5] + ', i am sorry to inform you that you had been removed from the dinner party due to a restaurant table issue, hope you still love me.')
print (message)
message = ('dear ' + names[1] + ', you are still invited to the dinner party.')
print (message)
message = ('dear ' + names[3] + ', you are still invited to the dinner party.')
print (message)
print (names)
list = []
list.append (names)
del list [0]
print (list)
