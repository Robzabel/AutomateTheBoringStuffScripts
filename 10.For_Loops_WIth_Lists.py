supplies = ['pen', 'stapler', 'book', 'paperclip']
for i in range(len(supplies)):
    print("number " + str(i + 1) + " is a " + supplies[i])


# Multiple assignment statements:
cat = [ 'fat', 'orange', 'loud'] # Here we have a list
#in order to assign the values into separate veriables you would need to write the following:
size = cat[0]
colour = cat[1]
volume = cat[2]

print(size)
print(colour)
print(volume)
#this can get tedious when lists are long so you can replace the method with the following:
house = [ 'brick', '2 bed', 'garden']
material, rooms, outside_area = house

print(material)
print(rooms)
print(outside_area)
#Much simpler, but you can go one step further and just assign the variables without having to make the initial list:

name, age, gender = 'Rob', '31', 'Male'

print(name)
print(age)
print(gender)

#Here is an example of using the multiple assignment statement to swap variables
a = 'aaa'
b = 'bbb'
a, b = b, a
print('a = ' + a)
print('B = ' + b)