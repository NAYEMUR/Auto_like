#how to creat a auto like,comment ,share BOT for facebook using python
import pyautogui
import time
pyautogui.FAILSAFE = False

for x in range(0, 2):
    time.sleep(5) #wait for 5 second
    #for like
    pyautogui.press('j') #read a post
    time.sleep(2)
    pyautogui.press('l') #react as like
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(2)
    #for comment
    pyautogui.press('c') #c for comment
    time.sleep(2)
    pyautogui.typewrite("this is comment",0.25)  #write a comment
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.press('tab') #leave from comment box
    time.sleep(2)
    #for share
    pyautogui.press('s') #s for share
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(2)
