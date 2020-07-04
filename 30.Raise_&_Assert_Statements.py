"""
*************
*           *
*           *
*           *
*************
"""
#this code can be broken easily because it doesnt sanatise the input
def boxPrint(symbol, width, height ):
    print(symbol * width)

    for i in range(height - 2):
        print(symbol + (" " * (width - 2)) + symbol)

    print(symbol * width)

#here is the same code but with raise statements to make sure the correct details are input

def boxPrint(symbol, width, height ):
    if len(symbol) != 1:
        raise Exception('"symbol" needs to be 1 character')
    if (width < 2) or (height <2):
        raise Exception('Width and heighthave to be greater than 1')
    print(symbol * width)

    for i in range(height - 2):
        print(symbol + (" " * (width - 2)) + symbol)

    print(symbol * width)

boxPrint('*', 15, 5 )


import traceback
try:
    raise Exception('This is the Error message')
except:
    errorfiler = open('/home/zabex/FolderWalk/errorLog.txt', 'a')
    errorfiler.write(traceback.format_exc())
    errorfiler.close()
    print('Traceback was written to errorLog.txt')

#assert statements
market_2nd = {'ns': 'green', 'ew':'red'}

def switchLights(intersection):
    for key in intersection.keys():
        if intersection[key] == 'green':
            intersection[key] == 'yellow'
        elif intersection[key] == 'yellow':
            intersection[key] == 'red'
        elif intersection[key] == 'red':
            intersection[key] == 'green'
    assert 'red' in intersection.values(), 'Neither light is red!' + str(intersection)

switchLights(market_2nd)
