"""def div42by(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print("You tried to divide by 0")
print(div42by(2))
print(div42by(12))
print(div42by(0))
print(div42by(1))"""

"""def div42by(divideBy):
    try:
        return 42 / divideBy
    except:
        print("You tried to divide by 0")
print(div42by(2))
print(div42by(12))
print(div42by(0))
print(div42by(1))"""

"""print("How many cats do you have?")
numCats = input()
if int(numCats) >=4 :
    print("Thats a lot of cats!")
else:
    print("Thats not too many cats.")"""

print("How many cats do you have?")
numCats = input()
if int(numCats) < 0:
   print("you have not entered a positive number")
else:
    try:
        if int(numCats) >=4 :
            print("Thats a lot of cats!")
        else:
            print("Thats not too many cats.")
    except ValueError:
        print("you did not enter a number")