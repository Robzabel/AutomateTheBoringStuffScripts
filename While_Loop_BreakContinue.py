name = ""
while True:
    print("Please type your name: ")
    name =input()
    if name == "your name":
        break
print("Thank You!\n\n")


spam = 0
while spam < 5:
    spam += 1
    if spam == 3:
        continue
    print("Spam is " + str(spam))

