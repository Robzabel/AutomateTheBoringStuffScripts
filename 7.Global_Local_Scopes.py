spam= 43 # global varialble
def spam():
    print(eggs)

eggs = 4
spam()


def meat():
    global eggs
    eggs = "hello"
    print(eggs)

print(eggs)
meat()