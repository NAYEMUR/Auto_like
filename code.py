import pyautogui
import time
pyautogui.FAILSAFE = False
for x in range(0, 5):
    time.sleep(5)
    pyautogui.press('j')
    pyautogui.press('l')
    pyautogui.press('enter')
