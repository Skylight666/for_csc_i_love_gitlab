import pyautogui
import time
time.sleep(3)
while 1:
    for y in range(101, 1030, 32):
        pyautogui.moveTo(0, y, 0)
        pyautogui.dragTo(1919, y, 1.25)
    pyautogui.click(x=720, y=700)
