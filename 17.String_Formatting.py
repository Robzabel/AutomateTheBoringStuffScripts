#the regular way:
name = 'Alice'
place = 'Main Street'
time = '6pm'
food = 'turnips'
print('Hello ' + name + ' You are invited to a party at ' + place + ' at ' + time + '. Please bring ' + food + '.')

#The format string way ( basically the same as C)
time = 6
print('Hello %s you are invited to a party at %s at %d. Please bring %s.' % ( name.lower().title(), place, time, food))

# the way from old boy in the other book
print(f'Hello {name.lower().title()} you are invited to a party at {place} at {time}. Please bring {food}.')