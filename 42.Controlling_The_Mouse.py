import pyautogui
print(pyautogui.size())#get the width and height
width, height = pyautogui.size()# use the multiple assignment technique for the width and height
print(height)
print(width)
print(pyautogui.position())#return the position of the mouse at the time of execution

#pyautogui.moveTo(0,0)#this function moves the mouse to the furthest top left position
pyautogui.moveTo(100,100, duration=2.5)# this gives the mouse an absolute position and specifies a time to get it there
pyautogui.moveRel(200,0, duration=3)#this moves the cursor to a relative position given in pixels
pyautogui.moveRel(-200,0, duration=3)
pyautogui.moveTo(2907, 1060, duration=3)
pyautogui.click(2907, 1060)

