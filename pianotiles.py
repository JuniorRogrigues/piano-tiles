import pyautogui
from time import sleep
import keyboard
import win32api
import win32con

pyautogui.click(1473, 452, duration=1)

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


while keyboard.is_pressed('1') == False:
   if pyautogui.pixelMatchesColor(1337, 366, (0,0,0)):
    click(1337, 366)
   if pyautogui.pixelMatchesColor(1421, 362, (0,0,0)):
    click(1421, 362)
   if pyautogui.pixelMatchesColor(1495, 366, (0,0,0)):
    click(1495, 366)
   if pyautogui.pixelMatchesColor(1585, 367, (0,0,0)):
    click(1585, 367)