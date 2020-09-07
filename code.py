#how to creat a auto like,comment ,share BOT for facebook using python
import pyautogui
import time
pyautogui.FAILSAFE = False

for x in range(0, 2):
    time.sleep(5)
    #for like
    pyautogui.press('j')
    time.sleep(2)
    pyautogui.press('l')
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(2)
    #for comment
    pyautogui.press('c')
    time.sleep(2)
    pyautogui.typewrite("this is comment",0.25)
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.press('tab')
    time.sleep(2)
    #for share
    pyautogui.press('s')
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(2)

