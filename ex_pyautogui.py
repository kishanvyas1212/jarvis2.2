import pyautogui
import time
import webbrowser
#  mouse functions 
time.sleep(2)
# print(pyautogui.size()) #will return resultion of the screen
# it will return actual position of cursor/mouse
print(pyautogui.position()) 
#  moves the mouse over time (2 second to move define position ), it will move to define cordinates
# pyautogui.moveTo(100,100,2)
# move the mouse to relative position of it
# pyautogui.moveRel(100,100,3)

# mouse click
#  below code is not take time to reach the position 
# pyautogui.click(1714,479,2,2,button='left')

# pyautogui.leftClick(1714,479) 
# pyautogui.doubleClick()
# pyautogui.tripleClick()
# pyautogui.rightClick()

#  using python scroll down and up, for scroll up need to give pixels to with + sign and for down add -
# pyautogui.scroll(-500)
# pyautogui.scroll(-800)

# mouse down or up to upto cordinate, to experience it, perform it on paint so you will get actual idea
# pyautogui.mouseDown(300,500,button='left') 
# pyautogui.moveTo(880,600,3)
# pyautogui.mouseUp()
# pyautogui.moveTo(900,700,3)
#  Lets draw spiral structure using python 

# time.sleep(1)
# pyautogui.moveTo(300,300,2)
# distance = 300
# while distance > 0:
#     pyautogui.dragRel(distance,0,1,button='left')
#     distance = distance - 20
#     pyautogui.dragRel(0,distance,1,button='left')
#     pyautogui.dragRel(-distance,0,1,button='left')
#     distance = distance -20
#     pyautogui.dragRel(0,-distance,1,button='left')
# time.sleep(2)



