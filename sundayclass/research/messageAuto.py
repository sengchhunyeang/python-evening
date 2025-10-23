import time

import pyautogui
x = 0
while x < 10:
    time.sleep(2)
    pyautogui.typewrite("Testing")
    pyautogui.press("enter")
    x+=1
